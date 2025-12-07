/**
 * @author Alessandro Ferrante
 * @description project StreetSignSense
 * @copyright 2025
 * @license MIT License 
 */

const CLASS_NAMES = ['prio_give_way', 'prio_stop', 'prio_priority_road', 'forb_speed_over_5', 'forb_speed_over_10', 'forb_speed_over_20', 'forb_speed_over_30', 'forb_speed_over_40', 'forb_speed_over_50', 'forb_speed_over_60', 'forb_speed_over_70', 'forb_speed_over_80', 'forb_speed_over_90', 'forb_speed_over_100', 'forb_speed_over_110', 'forb_speed_over_120', 'forb_speed_over_130', 'forb_no_entry', 'forb_no_parking', 'forb_no_stopping', 'forb_overtake_car', 'forb_overtake_trucks', 'forb_trucks', 'forb_turn_left', 'forb_turn_right', 'forb_weight_over_3.5t', 'forb_weight_over_7.5t', 'forb_u_turn', 'info_bus_station', 'info_crosswalk', 'info_highway', 'info_one_way', 'info_parking', 'info_taxi_parking', 'warn_children', 'warn_construction', 'warn_crosswalk', 'warn_cyclists', 'warn_left_curve', 'warn_right_curve', 'warn_domestic_animals', 'warn_other_dangers', 'warn_poor_road_surface', 'warn_roundabout', 'warn_sharp_left_curve', 'warn_sharp_right_curve', 'warn_slippery_road', 'warn_hump', 'warn_traffic_light', 'warn_tram', 'warn_two_way_traffic', 'warn_wild_animals', 'mand_bike_lane', 'mand_go_left', 'mand_go_left_right', 'mand_go_right', 'mand_go_straight', 'mand_go_straight_left', 'mand_go_straight_right', 'mand_pass_left', 'mand_pass_left_right', 'mand_pass_right', 'mand_roundabout'];

let MODEL_PATH = './demo/assets/models/StreetSignSenseY12s_tfjs_converted/model.json';
const MODEL_SIZE = 640;
let CONFIDENCE_THRESHOLD = 0.40; 
let IOU_THRESHOLD = 0.45;
let MAX_DETECTIONS = 30;  

const statusText = document.getElementById('status-text');
const loader = document.getElementById('loader');
const canvas = document.getElementById('canvas');
const displayCanvas = document.getElementById('displayCanvas');
const ctx = canvas.getContext('2d');
const displayCtx = displayCanvas.getContext('2d');

//? state
let model = null;
let isProcessing = false;
let webcamStream = null;
let isWebcamActive = false;
let isVideoAnalyzing = false;
let animationId = null;
let fpsCounter = { frames: 0, lastTime: performance.now() };
let currentImagePath = ''; 

let processedCanvas = null;
let inputTensor = null;

let videoDetectionsCache = {}; 
let totalVideoFrames = 0;
let currentAnalysisFrame = 0;

const VIDEO_FRAME_INTERVAL = 400; 
let lastDetections = []; 



function setAnimation(enabled) {
    const root = document.documentElement;
    if (enabled) {
        root.classList.remove('no-animations');
    } else {
        root.classList.add('no-animations');
    }
}


// - Funzione per aggiornare lo stato del caricamento
function setStatus(text, type = 'loading') {
    statusText.innerHTML = text;
    loader.style.display = type === 'loading' ? 'block' : 'none';
   statusText.style.color = '#00ffeeff';

    if (type === 'ready') {
        setAnimation(true);
        statusText.style.color = '#007bff';
    } else if(type === 'optimization'){
        statusText.style.color = '#fff200ff';
    } else if (type === 'error') {
        statusText.style.color = 'red';
    } else {
        statusText.style.color = '';
        isVideoAnalyzing = false;
        document.getElementById('analyze-video').innerHTML =  `${'<i class="fas fa-film"></i> '} ${' Analyze'} ${'<i class="fas fa-wand-magic-sparkles"></i>'}`;
        document.getElementById('analyze-video').disabled = false;
    }
    const statusDiv = document.getElementById('status');
    statusDiv.classList.remove('status-ready', 'status-error');
    
    if (type === 'ready') {
        statusDiv.classList.add('status-ready'); 
        document.getElementById('webcam-btn').disabled = false;
    } else if (type === 'error') {
        statusDiv.classList.add('status-error');
        document.getElementById('webcam-btn').disabled = true;
    } else {
            document.getElementById('webcam-btn').disabled = true;
    }
}

async function loadModel() {
    setAnimation(false);
    if (model) {
        model.dispose();
        model = null;
        tf.dispose(); 
        console.log('Modello precedente scaricato.');
    }

    setStatus(`${'Loading model '} ${'<i class="fas fa-download"></i>'}`, 'loading');
    
    const select = document.getElementById('model-select');
    MODEL_PATH = select.options[select.selectedIndex].getAttribute('data-path');
    console.log(MODEL_PATH); // ! log path
    try {
        model = await tf.loadGraphModel(MODEL_PATH);
        setStatus(`${' Model optimization'} ${'<i class="fa-solid fa-hexagon-nodes-bolt"></i>'}`, 'optimization');
        const dummy = tf.zeros([1, MODEL_SIZE, MODEL_SIZE, 3]); // ? tensore di zeri
        for(let i = 0; i < 3; i++) {
            const result = await model.executeAsync(dummy);
            if(Array.isArray(result)) {
                result.forEach(t => t.dispose());
            } else {
                result.dispose();
            }
        }
        dummy.dispose();
       
        setStatus(`${'System ready '} ${'<i class="fas fa-check"></i>'}`, 'ready');
        
    } catch (err) {
        console.error('Model loading error:', err);
        setStatus('Model loading error:', 'error');
        console.error(`Model loading error from: ${MODEL_PATH}. Check the file path.`);
    }
}

async function initializeApp() {
    try {
        const coverImage = displayCanvas.getContext('2d');
        const imagePath = './demo/assets/images/cover_image.png';
        const img = new Image();
        img.onload = function() { 
            coverImage.drawImage(img, 0, 0, displayCanvas.width, displayCanvas.height); 
            currentImagePath = imagePath;   
        };
        img.src = imagePath;
        await tf.setBackend('webgl');
        await tf.ready();
        
        //!console.log('Backend attuale:', tf.getBackend());
        
        tf.env().set('WEBGL_PACK', true);
        tf.env().set('WEBGL_FORCE_F16_TEXTURES', false);
        tf.env().set('WEBGL_EXP_CONV', true);

        processedCanvas = document.createElement('canvas');
        processedCanvas.width = MODEL_SIZE;
        processedCanvas.height = MODEL_SIZE;
        setupEventListeners();
        await loadModel();
        
    } catch (err) {
        console.error('Errore inizializzazione TF.js:', err);
        setStatus('Errore inizializzazione libreria', 'error');
    }
}

function preprocessImage(source, drawToDisplay = true) {
    const ctx = processedCanvas.getContext('2d');
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, MODEL_SIZE, MODEL_SIZE);
    
    const srcW = source.videoWidth || source.naturalWidth || source.width;
    const srcH = source.videoHeight || source.naturalHeight || source.height;
    
    if (!srcW || !srcH) return null;
    
    const scale = Math.min(MODEL_SIZE / srcW, MODEL_SIZE / srcH);
    const scaledW = srcW * scale;
    const scaledH = srcH * scale;
    const padX = (MODEL_SIZE - scaledW) / 2;
    const padY = (MODEL_SIZE - scaledH) / 2;
    
    ctx.drawImage(source, padX, padY, scaledW, scaledH);
    
    if (drawToDisplay) {
        const displayW = displayCanvas.width;
        const displayH = displayCanvas.height;
        
        displayCtx.fillStyle = '#00000004';
        displayCtx.fillRect(0, 0, displayW, displayH);
        
        const displayScale = Math.min(displayW / srcW, displayH / srcH);
        const displayScaledW = srcW * displayScale;
        const displayScaledH = srcH * displayScale;
        const displayPadX = (displayW - displayScaledW) / 2;
        const displayPadY = (displayH - displayScaledH) / 2;
        
        displayCtx.drawImage(source, displayPadX, displayPadY, displayScaledW, displayScaledH);
    }
    
    return { scale, padX, padY, srcW, srcH };
}


// - DETECTION 

async function detectObjects(source) {
    if (!model || isProcessing) return [];
    
    isProcessing = true;
    const startTime = performance.now();

    try {
        // ? webcm = false (non disegna) Upload = true (disegna)
        const shouldDraw = !isWebcamActive; 
        const preprocessInfo = preprocessImage(source, shouldDraw);
        
        if (!preprocessInfo) {
            isProcessing = false;
            return [];
        }

        if (inputTensor) inputTensor.dispose();
        inputTensor = tf.browser.fromPixels(processedCanvas)
            .toFloat()
            .div(255.0)
            .expandDims(0);
        
            const outputs = await model.executeAsync(inputTensor);
        let predictions;
        
        if (Array.isArray(outputs)) {
            predictions = outputs[0];
            outputs.slice(1).forEach(t => t.dispose());
        } else {
            predictions = outputs;
        }

        const data = await predictions.array();
        predictions.dispose();
        const detections = processDetections(data[0], preprocessInfo);

        const timeEl = document.getElementById('inference-time');
        if (timeEl) timeEl.textContent = Math.round(performance.now() - startTime);

        isProcessing = false;
        return detections;

    } catch (err) {
        console.error('Detection error:', err);
        isProcessing = false; //!
        return [];
    }
}

// - PROCESSING DETECTIONS

function processDetections(rawDetections, preprocessInfo) {
    const validDetections = [];
    
    for (let i = 0; i < rawDetections.length; i++) {
        const det = rawDetections[i];
        if (!det) continue;

        const [x1, y1, x2, y2, confidence, classId] = det;
        
        if (confidence < CONFIDENCE_THRESHOLD) continue;
        
        const w = x2 - x1;
        const h = y2 - y1;
        
        const intClassId = Math.floor(Math.max(0, Math.min(CLASS_NAMES.length - 1, classId)));
        
        validDetections.push({
            x: x1, y: y1, w: w, h: h,
            score: confidence,
            classId: intClassId,
            className: CLASS_NAMES[intClassId] || `class_${intClassId}`
        });
    }
    
    validDetections.sort((a, b) => b.score - a.score);
    return validDetections.slice(0, MAX_DETECTIONS);
}


// - RENDERING

function drawDetections(detections) {
    const drawW = canvas.width;
    const drawH = canvas.height;
    ctx.clearRect(0, 0, drawW, drawH);
    
    document.getElementById('obj-count').textContent = detections.length;
    
    const listHtml = detections.map((det, i) => 
        `${i+1}. ${det.className} (${(det.score * 100).toFixed(1)}%)`
    ).join(' | ');
    document.getElementById('detections-list').innerHTML = listHtml || 'No objects detected';
    
    const scaleX = drawW / MODEL_SIZE;
    const scaleY = drawH / MODEL_SIZE;
    
    detections.forEach((det, index) => {
        // ? riscala le coordinate dal modello 640x640 al canvas di disegno
        const drawX = det.x * scaleX;
        const drawY = det.y * scaleY;
        const drawW_box = det.w * scaleX;
        const drawH_box = det.h * scaleY;
        
        const hue = (det.classId * 137) % 360;
        const color = `hsl(${hue}, 80%, 60%)`; 
        
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.strokeRect(drawX, drawY, drawW_box, drawH_box);
        
        ctx.fillStyle = color;
        const markerSize = 4;
        ctx.fillRect(drawX - markerSize/2, drawY - markerSize/2, markerSize, markerSize);
        ctx.fillRect(drawX + drawW_box - markerSize/2, drawY - markerSize/2, markerSize, markerSize);
        ctx.fillRect(drawX - markerSize/2, drawY + drawH_box - markerSize/2, markerSize, markerSize);
        ctx.fillRect(drawX + drawW_box - markerSize/2, drawY + drawH_box - markerSize/2, markerSize, markerSize);
        
        const label = `${det.className} ${(det.score * 100).toFixed(1)}%`;
        const fontSize = Math.max(10, Math.min(14, drawW_box * 0.08));
        ctx.font = `800 ${fontSize}px 'Poppins', sans-serif`; 
        
        const textMetrics = ctx.measureText(label);
        const textWidth = textMetrics.width;
        const textHeight = fontSize;
        const padding = 3;
        
        let labelX = drawX;
        let labelY = drawY - 5;
        
        if (labelY - textHeight < 0) {
            labelY = drawY + textHeight + 5;
        }
        
        ctx.fillStyle = color;
        ctx.globalAlpha = 0.8;
        ctx.fillRect(labelX, labelY - textHeight, textWidth + padding * 2, textHeight + padding);
        
        ctx.globalAlpha = 1;
        ctx.fillStyle = '#000'; 
        ctx.fillText(label, labelX + padding, labelY - 1); 
    });
        
}

function resizeCanvas() {
    const container = document.getElementById('detection-container');
    const width = container.clientWidth;
    const height = container.clientHeight;

    if (canvas.width !== width || canvas.height !== height) {
        canvas.width = width;
        canvas.height = height;
        displayCanvas.width = width;
        displayCanvas.height = height;
        
        // ridisegna il frame corrente se presente
        const video = document.getElementById('video-element');
        if (isWebcamActive && webcamStream) {
              
        } else if (!video.paused && isVideoAnalyzing) {
           
        } else {
            // l'ultima immagine o video frame
            const source = video.srcObject ? video : (video.src ? video : document.getElementById('demo-img-hidden') || displayCanvas);
            if(source) {
                preprocessImage(source); 
                ctx.clearRect(0, 0, width, height);
            }
        }
    }
}


// - FPS COUNTER
function updateFPS() {
    fpsCounter.frames++;
    const now = performance.now();
    const elapsed = now - fpsCounter.lastTime;
    
    if (elapsed >= 1000) {
        const fps = Math.round((fpsCounter.frames * 1000) / elapsed);
        document.getElementById('fps').textContent = fps;
        fpsCounter.frames = 0;
        fpsCounter.lastTime = now;
    }
}


// - WEBCAM HANDLING
async function toggleWebcam() {
    if (isWebcamActive) {
        stopWebcam();
        document.getElementById('fps').textContent = 0;
        setAnimation(true);
    } else {
        await startWebcam();
    }
}

async function startWebcam() {
    try {
        setAnimation(false);
        resizeCanvas();
        const constraints = {
            video: {
                width: { ideal: 1280, max: 1920 },
                height: { ideal: 720, max: 1080 },
                facingMode: 'environment'
            }
        };
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        displayCtx.clearRect(0, 0, displayCanvas.width, displayCanvas.height);

        webcamStream = await navigator.mediaDevices.getUserMedia(constraints);
        
        const video = document.createElement('video');
        video.srcObject = webcamStream;
        video.play();
        
        video.onloadedmetadata = () => {
            isWebcamActive = true;
            const webcamBtn = document.getElementById('webcam-btn');
            webcamBtn.innerHTML = `${'<i class="fas fa-stop"></i>'} ${' Stop Webcam'}`;
            webcamLoop(video);
        };
        
    } catch (err) {
        setAnimation(true);
        console.error('Webcam error:', err);
        console.error('Impossibile accedere alla webcam', err);
    }
}

function stopWebcam() {
    isWebcamActive = false;
    isProcessing = false;
    if (animationId) {
        cancelAnimationFrame(animationId);
        animationId = null;
    }
    if (webcamStream) {
        webcamStream.getTracks().forEach(track => track.stop());
        webcamStream = null;
    }
    const webcamBtn = document.getElementById('webcam-btn');
    webcamBtn.innerHTML = `${'<i class="fas fa-video"></i>'} ${' Webcam'}`;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    displayCtx.clearRect(0, 0, displayCanvas.width, displayCanvas.height);
}

function drawVideoFrame(video) {
    const srcW = video.videoWidth || video.naturalWidth || video.width;
    const srcH = video.videoHeight || video.naturalHeight || video.height;

    if (!srcW || !srcH) return;

    const displayW = displayCanvas.width;
    const displayH = displayCanvas.height;

    const scale = Math.min(displayW / srcW, displayH / srcH);
    const scaledW = srcW * scale;
    const scaledH = srcH * scale;
    const x = (displayW - scaledW) / 2;
    const y = (displayH - scaledH) / 2;

    displayCtx.fillStyle = '#00000004';
    displayCtx.fillRect(0, 0, displayW, displayH);
    displayCtx.drawImage(video, 0, 0, srcW, srcH, x, y, scaledW, scaledH);

    updateFPS();
}

async function webcamLoop(video) {
    if (!isWebcamActive) return;
    // pulizia vecchi bdngbox
    const drawW = canvas.width;
    const drawH = canvas.height;
    ctx.clearRect(0, 0, drawW, drawH);

    // show video
    drawVideoFrame(video);

    if (lastDetections.length > 0) {
        drawDetections(lastDetections);
    }
    // detection
    if (video.readyState === video.HAVE_ENOUGH_DATA && !isProcessing) {
        runDetectionBackground(video);
    }
    requestAnimationFrame(() => webcamLoop(video));
}

function runDetectionBackground(video) {
    detectObjects(video).then((detections) => {
        lastDetections = detections || [];  
    }).catch((err) => {
        console.error(err);
    });
}


// - FILE HANDLING

async function handleFile(file) {
    currentImagePath = '';
    if (!file) return;
    isVideoAnalyzing = false;
    stopWebcam();
    
    if (file.type.startsWith('image/')) {
        await handleImage(file);
    } else if (file.type.startsWith('video/')) {
        await handleVideo(file);
    }
}

async function handleImage(fileOrUrl) {
    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.onload = async () => {
        resizeCanvas(); 
        const detections = await detectObjects(img);
        drawDetections(detections);
       
        const hiddenImg = document.getElementById('demo-img-hidden') || document.createElement('img');
        hiddenImg.id = 'demo-img-hidden';
        hiddenImg.src = img.src;
        hiddenImg.style.display = 'none';
        if (!document.getElementById('demo-img-hidden')) document.body.appendChild(hiddenImg);
    };
    img.onerror = () => {
        console.warn('Errore caricamento immagine:', fileOrUrl);
    };
    if (typeof fileOrUrl === 'string') {
        img.src = fileOrUrl;
    } else {
        img.src = URL.createObjectURL(fileOrUrl);
    }
}

async function handleVideo(file) {
    resizeCanvas();
    const video = document.getElementById('video-element');
    video.src = URL.createObjectURL(file);
    document.getElementById('video-controls').classList.remove('hidden');
    
    video.onloadedmetadata = () => {
        document.getElementById('video-seek').max = video.duration;
        document.getElementById('video-seek').value = 0;
        document.getElementById('analyze-video').disabled = false;
        isVideoAnalyzing = true;
        preAnalyzeVideo(video);
    };
    video.onseeked = async () => {
        if (!isVideoAnalyzing) {
            const detections = await detectObjects(video);
            drawDetections(detections);
        }
    };
}

// - Funzione per la riproduzione con detections memorizzate
async function playbackLoop() {
    const video = document.getElementById('video-element');
    if(video.ended) {
        document.getElementById('play-pause').innerHTML = `${'<i class="fas fa-film"></i> <i class="fas fa-play"></i>'}`;
        document.getElementById('fps').textContent = 0;
    }
    if (video.paused || video.ended) return;

    resizeCanvas();
    
    const displayW = displayCanvas.width;
    const displayH = displayCanvas.height;
    const srcW = video.videoWidth;
    const srcH = video.videoHeight;
    
    // scaling per letterbox
    const scale = Math.min(displayW / srcW, displayH / srcH);
    const scaledW = srcW * scale;
    const scaledH = srcH * scale;
    const padX = (displayW - scaledW) / 2;
    const padY = (displayH - scaledH) / 2;
    
    displayCtx.fillStyle = '#00000004';
    displayCtx.fillRect(0, 0, displayW, displayH);
    displayCtx.drawImage(video, padX, padY, scaledW, scaledH);
    
    // recupera le detections dal cache e scalale al canvas di disegno
    const frameIndex = Math.round(video.currentTime * 1000 / VIDEO_FRAME_INTERVAL);
    const detections = videoDetectionsCache[frameIndex] || [];
    
    document.getElementById('video-seek').value = video.currentTime;
    // scala le detections dal modello 640x640 al canvas
    const scaleX = displayW / 640;
    const scaleY = displayH / 640;
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    detections.forEach((det) => {
        const drawX = det.x * scaleX;
        const drawY = det.y * scaleY;
        const drawW_box = det.w * scaleX;
        const drawH_box = det.h * scaleY;
        
        const hue = (det.classId * 137) % 360;
        const color = `hsl(${hue}, 80%, 60%)`;
        
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.strokeRect(drawX, drawY, drawW_box, drawH_box);
        
        const label = `${det.className} ${(det.score * 100).toFixed(1)}%`;
        const fontSize = 12;
        ctx.font = `800 ${fontSize}px 'Poppins', sans-serif`;
        
        const textMetrics = ctx.measureText(label);
        const textWidth = textMetrics.width;
        const padding = 3;
        
        ctx.fillStyle = color;
        ctx.globalAlpha = 0.8;
        ctx.fillRect(drawX, drawY - fontSize - padding * 2, textWidth + padding * 2, fontSize + padding);
        
        ctx.globalAlpha = 1;
        ctx.fillStyle = '#000';
        ctx.fillText(label, drawX + padding, drawY - padding);
    });
    updateFPS();
    requestAnimationFrame(() => playbackLoop());
}

// - Modifica preAnalyzeVideo
/**
 * Analizza il video frame per frame, aggiorna lo stato globale delle detection e aggiorna direttamente l'interfaccia utente.
 */
async function preAnalyzeVideo(video) {
    document.getElementById('analyze-video').disabled = true; 
    setAnimation(false);
    videoDetectionsCache = {};
    currentAnalysisFrame = 0;
    
    const frameInterval = VIDEO_FRAME_INTERVAL;
    let currentTime = 0;
    
    while (currentTime < video.duration && isVideoAnalyzing) {
        video.currentTime = currentTime;
        
        await new Promise(resolve => {
            const onSeeked = () => {
                video.removeEventListener('seeked', onSeeked);
                resolve();
            };
            video.addEventListener('seeked', onSeeked);
        });
        
        const detections = await detectObjects(video);
        const frameIndex = Math.round(currentTime * 1000 / frameInterval);
        videoDetectionsCache[frameIndex] = detections;
        currentAnalysisFrame++;
        const progress = Math.round((currentTime / video.duration) * 100);
        document.getElementById('analyze-video').innerHTML = `${'<i class="fa-solid fa-hourglass-half"></i>'} ${progress}%`;
        document.getElementById('video-seek').value = video.currentTime;

        currentTime += frameInterval / 1000;
        updateFPS();
    }
    
    if (isVideoAnalyzing) {
        document.getElementById('analyze-video').innerHTML = `${'<i class="fas fa-film"></i> '}  ${' Video Analyzed '}${'<i class="fas fa-check"></i>'}`;
        video.currentTime = 0;
        video.play();
        playbackLoop();
        document.getElementById('play-pause').innerHTML = `${'<i class="fas fa-film"></i> <i class="fas fa-pause"></i>'}`;
    }
    
}


// - DEMO IMAGE
async function loadDemoImage() {
    stopWebcam();

    window._demoImagesState = window._demoImagesState || {
        list: [],
        order: [],
        idx: 0,
        initialized: false
    };
    currentImagePath = '';
    const state = window._demoImagesState;
    const folderPath = './demo/assets/images/demo_images/';

    function shuffle(arr) {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }

    async function fetchImageList() {
        
        try {
            const res = await fetch(folderPath, { cache: 'no-store' });
            if (res.ok) {
                const text = await res.text();
                const matches = [...text.matchAll(/href=["']([^"']+\.(?:jpg|jpeg|png|gif|webp))["']/ig)];
                const files = matches.map(m => m[1]).filter(Boolean).map(name => {
                    if (name.startsWith('http') || name.startsWith('/')) return name;
                    return folderPath + name.replace(/^\.\// , '');
                });
                if (files.length) return files;
            }
        } catch (e) { /* ignore */ }

        return [];
    }

    if (!state.initialized) {
        const list = await fetchImageList();
        state.list = Array.from(new Set((list || []).filter(Boolean)));
        if (!state.list.length) {
            state.list = ['https://placehold.co/640x640/eeeeee04/333?text=Demo+Image'];
        }
        state.order = [...state.list];
        shuffle(state.order);
        state.idx = 0;
        state.initialized = true;
    }

    if (!state.order.length) {
        console.warn('Nessuna demo image trovata.');
        return;
    }

    const imgUrl = state.order[state.idx];
    state.idx = (state.idx + 1) % state.order.length;

    handleImage(imgUrl);
}


// - EVENT LISTENERS

function setupEventListeners() {
    document.getElementById('load-model-btn').addEventListener('click', loadModel);
    
    document.getElementById('file-upload').addEventListener('change', (e) => {
        handleFile(e.target.files[0]);
    });
    
    document.getElementById('camera-capture').addEventListener('change', (e) => {
        handleFile(e.target.files[0]);
    });
    
    document.getElementById('webcam-btn').addEventListener('click', toggleWebcam);
    
    document.getElementById('demo-btn').addEventListener('click', loadDemoImage);
    
    document.getElementById('confidence').addEventListener('input', (e) => {
        CONFIDENCE_THRESHOLD = e.target.value / 100;
        document.getElementById('conf-value').textContent = CONFIDENCE_THRESHOLD.toFixed(2);
    });
    
    document.getElementById('iou').addEventListener('input', (e) => {
        IOU_THRESHOLD = e.target.value / 100;
        document.getElementById('iou-value').textContent = IOU_THRESHOLD.toFixed(2);
    });
    
    document.getElementById('max-det').addEventListener('change', (e) => {
        MAX_DETECTIONS = parseInt(e.target.value);
    });
    
    document.getElementById('apply-settings').addEventListener('click', async () => {
        const video = document.getElementById('video-element');
        let source = null;
        if (isWebcamActive && webcamStream) {
            return;
        } else if (video.src && !video.paused) {
            source = video;
        }else if(video.src && video.paused){
            source = video;
            isVideoAnalyzing = false;
            document.getElementById('analyze-video').innerHTML =  `${'<i class="fas fa-film"></i> '} ${' Analyze'} ${'<i class="fas fa-wand-magic-sparkles"></i>'}`;
            
            document.getElementById('analyze-video').disabled = false;
        } else if(currentImagePath === './demo/assets/images/cover_image.png'){
            return;
        } else {
            source = document.getElementById('demo-img-hidden') || displayCanvas;
        }
        const detections = await detectObjects(source);
        drawDetections(detections);
    });
    
    document.getElementById('play-pause').addEventListener('click', () => {
        const video = document.getElementById('video-element');
        if (video.paused) {
            if (isVideoAnalyzing) {
                video.play();
                playbackLoop();
            } else{
                video.play();
            }
            document.getElementById('play-pause').innerHTML = `${'<i class="fas fa-film"></i> <i class="fas fa-pause"></i>'}`;
        } else {
            video.pause();
            document.getElementById('play-pause').innerHTML = `${'<i class="fas fa-film"></i> <i class="fas fa-play"></i>'}`;
        }
    });
    
    document.getElementById('analyze-video').addEventListener('click', () => {
        const video = document.getElementById('video-element');
        const btn = document.getElementById('analyze-video');
        if (isVideoAnalyzing) {
            isVideoAnalyzing = false;
            btn.innerHTML = `${'<i class="fas fa-film"> </i> <i class="fas fa-wand-magic-sparkles"></i>'} ${' Analyze'}`;
            video.pause();
        } else {
            isVideoAnalyzing = true;
            btn.innerHTML = `${'<i class="fas fa-stop"></i>'} ${' Video'}`;
            preAnalyzeVideo(video);
        }
    });
    
    document.getElementById('video-seek').addEventListener('input', (e) => {
        const video = document.getElementById('video-element');
        video.currentTime = e.target.value;
    });

    new ResizeObserver(resizeCanvas).observe(document.getElementById('detection-container'));
}
let lastAnalysisTime = 0;
const ANALYSIS_INTERVAL = 10; // analizza ogni 100ms (crca 10 FPS)

async function analyzeVideoLoop(video) {
    if (!isVideoAnalyzing || video.paused || video.ended) {
        isVideoAnalyzing = false;
        document.getElementById('analyze-video').innerHTML = `${'<i class="fas fa-film"> </i> <i class="fas fa-wand-magic-sparkles"></i>'} ${' Analyze'}`;
        return;
    }
    resizeCanvas(); 
    
    const now = performance.now();
    if (now - lastAnalysisTime >= ANALYSIS_INTERVAL && video.readyState >= 2 && !isProcessing) {
        const detections = await detectObjects(video);
        drawDetections(detections);
        lastAnalysisTime = now;
    }
    
    
    requestAnimationFrame(() => analyzeVideoLoop(video));
}

const iconInfo = document.getElementById("info");
const iconInfoClose = document.getElementById("info-close");
const infoModal = document.getElementById("infoModal");
const closeInfoButton = document.getElementById("closeInfoButton");
const disclaimerModal = document.getElementById("disclaimerModal");
const closeDisclaimerButton= document.getElementById("closeDisclaimerButton");
iconInfo.addEventListener("click", () => {
    infoModal.style.display = "block";
    iconInfo.style.display = "none";
    iconInfoClose.style.display = "block";
});

closeInfoButton.addEventListener("click", () => {
    infoModal.style.display = "none";
    iconInfo.style.display = "block";
    iconInfoClose.style.display = "none";
});

var disclaimerClosed = false;
closeDisclaimerButton.addEventListener("click", () => {
    disclaimerModal.style.display = "none";
    disclaimerClosed = true;
    initializeApp();
});
