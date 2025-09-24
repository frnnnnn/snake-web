# 2. CSS ESPECTACULAR - ESTILO VIDEOJUEGO AAA
css_content = '''/* 🎮 SNAKE AI WEB - ESTILOS VIDEOJUEGO AAA */
/* Futurista, moderno, con efectos visuales espectaculares */

/* Variables CSS para tema futurista */
:root {
    /* Colores principales */
    --primary-bg: #0a0a0f;
    --secondary-bg: #1a1a2e;
    --accent-bg: #16213e;
    --card-bg: #1e2749;
    --surface-bg: #252a4a;
    
    /* Colores neón */
    --neon-cyan: #00ffff;
    --neon-purple: #8a2be2;
    --neon-green: #39ff14;
    --neon-pink: #ff10f0;
    --neon-orange: #ff6600;
    --neon-blue: #0080ff;
    --neon-yellow: #ffff00;
    
    /* Colores de texto */
    --text-primary: #ffffff;
    --text-secondary: #b0b3d6;
    --text-accent: #7dd3fc;
    --text-success: #10b981;
    --text-warning: #f59e0b;
    --text-error: #ef4444;
    
    /* Gradientes */
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --gradient-cyber: linear-gradient(45deg, #00ffff 0%, #8a2be2 50%, #ff10f0 100%);
    --gradient-neon: linear-gradient(90deg, #39ff14 0%, #00ffff 50%, #8a2be2 100%);
    
    /* Sombras */
    --shadow-glow: 0 0 20px rgba(0, 255, 255, 0.3);
    --shadow-deep: 0 10px 30px rgba(0, 0, 0, 0.5);
    --shadow-neon: 0 0 40px currentColor;
    
    /* Fuentes */
    --font-primary: 'Orbitron', monospace;
    --font-secondary: 'Exo 2', sans-serif;
    
    /* Transiciones */
    --transition-fast: 0.2s ease;
    --transition-smooth: 0.4s cubic-bezier(0.4, 0.0, 0.2, 1);
    --transition-bounce: 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

/* Reset y base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-secondary);
    background: var(--primary-bg);
    color: var(--text-primary);
    overflow-x: hidden;
    position: relative;
    min-height: 100vh;
    background-image: 
        radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
        radial-gradient(circle at 40% 80%, rgba(120, 219, 255, 0.3) 0%, transparent 50%);
    animation: backgroundPulse 20s ease-in-out infinite;
}

@keyframes backgroundPulse {
    0%, 100% { filter: hue-rotate(0deg) brightness(1); }
    50% { filter: hue-rotate(30deg) brightness(1.2); }
}

/* Fondo de partículas animado */
#particles-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -2;
    background: 
        radial-gradient(2px 2px at 20% 30%, var(--neon-cyan), transparent),
        radial-gradient(2px 2px at 40% 70%, var(--neon-purple), transparent),
        radial-gradient(1px 1px at 90% 40%, var(--neon-pink), transparent),
        radial-gradient(1px 1px at 10% 60%, var(--neon-green), transparent);
    background-size: 100px 100px, 80px 80px, 60px 60px, 120px 120px;
    animation: particleFloat 15s linear infinite;
}

@keyframes particleFloat {
    0% { transform: translate(0, 0); opacity: 0.7; }
    50% { transform: translate(-20px, -20px); opacity: 1; }
    100% { transform: translate(-40px, -40px); opacity: 0.7; }
}

/* Scanlines futuristas */
#scanlines {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: repeating-linear-gradient(
        0deg,
        transparent 0px,
        rgba(0, 255, 255, 0.03) 1px,
        transparent 2px
    );
    animation: scanlineMove 2s linear infinite;
}

@keyframes scanlineMove {
    0% { transform: translateY(0); }
    100% { transform: translateY(4px); }
}

/* Pantalla de carga épica */
.loading-active {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at center, #1a1a2e 0%, #0a0a0f 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    animation: loadingPulse 3s ease-in-out infinite;
}

@keyframes loadingPulse {
    0%, 100% { background: radial-gradient(circle at center, #1a1a2e 0%, #0a0a0f 100%); }
    50% { background: radial-gradient(circle at center, #2a2a3e 0%, #1a1a1f 100%); }
}

.loading-container {
    text-align: center;
    transform: scale(0.9);
    animation: loadingScale 2s ease-in-out infinite alternate;
}

@keyframes loadingScale {
    0% { transform: scale(0.9) rotateY(0deg); }
    100% { transform: scale(1) rotateY(5deg); }
}

/* Logo IA animado */
.ai-logo {
    position: relative;
    width: 200px;
    height: 200px;
    margin: 0 auto 30px;
}

.logo-core {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80px;
    height: 80px;
    background: var(--gradient-cyber);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-glow);
    animation: logoCorePulse 2s ease-in-out infinite;
}

@keyframes logoCorePulse {
    0%, 100% { 
        transform: translate(-50%, -50%) scale(1); 
        box-shadow: 0 0 20px var(--neon-cyan);
    }
    50% { 
        transform: translate(-50%, -50%) scale(1.1); 
        box-shadow: 0 0 40px var(--neon-purple);
    }
}

.logo-core i {
    font-size: 2.5rem;
    color: var(--text-primary);
    animation: brainThink 3s ease-in-out infinite;
}

@keyframes brainThink {
    0%, 100% { transform: rotateY(0deg); color: var(--text-primary); }
    25% { transform: rotateY(90deg); color: var(--neon-cyan); }
    50% { transform: rotateY(180deg); color: var(--neon-purple); }
    75% { transform: rotateY(270deg); color: var(--neon-pink); }
}

/* Anillos orbitales */
.logo-rings {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.ring {
    position: absolute;
    border: 2px solid;
    border-radius: 50%;
    animation: ringRotate 10s linear infinite;
}

.ring-1 {
    top: 20px;
    left: 20px;
    right: 20px;
    bottom: 20px;
    border-color: var(--neon-cyan);
    animation-duration: 8s;
    animation-direction: reverse;
}

.ring-2 {
    top: 40px;
    left: 40px;
    right: 40px;
    bottom: 40px;
    border-color: var(--neon-purple);
    animation-duration: 12s;
}

.ring-3 {
    top: 60px;
    left: 60px;
    right: 60px;
    bottom: 60px;
    border-color: var(--neon-pink);
    animation-duration: 15s;
    animation-direction: reverse;
}

@keyframes ringRotate {
    0% { transform: rotate(0deg); border-style: solid; }
    25% { border-style: dashed; }
    50% { transform: rotate(180deg); border-style: dotted; }
    75% { border-style: dashed; }
    100% { transform: rotate(360deg); border-style: solid; }
}

/* Título con efecto glitch */
.loading-title {
    margin-bottom: 30px;
}

.glitch {
    font-family: var(--font-primary);
    font-size: 3.5rem;
    font-weight: 900;
    text-transform: uppercase;
    position: relative;
    color: var(--text-primary);
    letter-spacing: 0.2em;
    animation: glitch 2s linear infinite;
}

@keyframes glitch {
    2%, 64% { transform: translate(2px, 0) skew(0deg); }
    4%, 60% { transform: translate(-2px, 0) skew(0deg); }
    62% { transform: translate(0, 0) skew(5deg); }
}

.glitch:before {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    color: var(--neon-cyan);
    z-index: -1;
    animation: glitch-1 2s linear infinite;
}

.glitch:after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    color: var(--neon-pink);
    z-index: -2;
    animation: glitch-2 2s linear infinite;
}

@keyframes glitch-1 {
    1%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
        transform: translate(0, 0);
        clip-path: inset(0);
    }
    20%, 22%, 24% {
        transform: translate(-2px, 0);
        clip-path: inset(0 0 95% 0);
    }
    55% {
        transform: translate(-2px, 0);
        clip-path: inset(0 0 85% 0);
    }
}

@keyframes glitch-2 {
    1%, 65%, 67%, 69%, 97%, 100% {
        transform: translate(0, 0);
        clip-path: inset(0);
    }
    66%, 68% {
        transform: translate(2px, 0);
        clip-path: inset(85% 0 0 0);
    }
    98% {
        transform: translate(2px, 0);
        clip-path: inset(95% 0 0 0);
    }
}

.subtitle {
    display: block;
    font-size: 1.5rem;
    color: var(--neon-purple);
    margin-top: 10px;
    animation: subtitleGlow 3s ease-in-out infinite;
}

@keyframes subtitleGlow {
    0%, 100% { text-shadow: 0 0 10px var(--neon-purple); }
    50% { text-shadow: 0 0 20px var(--neon-cyan), 0 0 30px var(--neon-purple); }
}

/* Barra de carga futurista */
.loading-bar {
    width: 400px;
    height: 8px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    margin: 30px auto;
    position: relative;
    overflow: hidden;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
}

.loading-progress {
    height: 100%;
    background: var(--gradient-cyber);
    border-radius: 20px;
    width: 0%;
    animation: loadingProgress 4s ease-in-out infinite;
    position: relative;
}

@keyframes loadingProgress {
    0% { width: 0%; }
    50% { width: 70%; }
    100% { width: 100%; }
}

.loading-progress::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.4) 50%, transparent 100%);
    animation: shine 2s ease-in-out infinite;
}

@keyframes shine {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Texto de carga con efecto typing */
.loading-text {
    font-size: 1.1rem;
    color: var(--text-secondary);
    margin: 20px 0;
    min-height: 1.5em;
}

.typing-text {
    overflow: hidden;
    border-right: 2px solid var(--neon-cyan);
    white-space: nowrap;
    animation: typing 3s steps(40) infinite, blink-caret 0.75s step-end infinite;
}

@keyframes typing {
    0% { width: 0; }
    50% { width: 100%; }
    100% { width: 0; }
}

@keyframes blink-caret {
    0%, 50% { border-color: var(--neon-cyan); }
    51%, 100% { border-color: transparent; }
}

/* Especificaciones técnicas */
.tech-specs {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    opacity: 0;
    animation: specsFadeIn 1s ease-in-out 2s forwards;
}

@keyframes specsFadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

.spec-item {
    display: flex;
    align-items: center;
    gap: 15px;
    font-size: 0.9rem;
    color: var(--text-secondary);
    background: rgba(255, 255, 255, 0.05);
    padding: 10px 20px;
    border-radius: 25px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
}

.spec-item i {
    color: var(--neon-cyan);
    font-size: 1.2rem;
}

/* Ocultar interfaz durante carga */
.interface-hidden {
    display: none;
}

/* Header principal */
.game-header {
    position: relative;
    background: linear-gradient(135deg, var(--secondary-bg) 0%, var(--accent-bg) 100%);
    border-bottom: 2px solid var(--neon-cyan);
    padding: 20px 30px;
    backdrop-filter: blur(20px);
    box-shadow: 
        0 4px 20px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.header-glow {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--gradient-cyber);
    opacity: 0.1;
    animation: headerGlow 8s ease-in-out infinite;
}

@keyframes headerGlow {
    0%, 100% { opacity: 0.1; transform: scaleY(1); }
    50% { opacity: 0.2; transform: scaleY(1.02); }
}

.header-content {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1600px;
    margin: 0 auto;
}

/* Logo principal */
.logo-section {
    display: flex;
    align-items: center;
    gap: 20px;
}

.main-logo {
    display: flex;
    align-items: center;
    gap: 15px;
    font-family: var(--font-primary);
}

.main-logo i {
    font-size: 2.5rem;
    background: var(--gradient-cyber);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: logoFloat 3s ease-in-out infinite;
}

@keyframes logoFloat {
    0%, 100% { transform: translateY(0px) rotateZ(0deg); }
    50% { transform: translateY(-5px) rotateZ(5deg); }
}

.logo-text .primary {
    font-size: 2rem;
    font-weight: 900;
    color: var(--text-primary);
    text-shadow: 0 0 10px var(--neon-cyan);
}

.logo-text .secondary {
    font-size: 2rem;
    font-weight: 700;
    background: var(--gradient-neon);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle-badge {
    background: rgba(138, 43, 226, 0.2);
    padding: 8px 16px;
    border-radius: 20px;
    border: 1px solid var(--neon-purple);
    backdrop-filter: blur(10px);
}

.subtitle-badge span {
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--neon-purple);
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* Estadísticas del header */
.header-stats {
    display: flex;
    gap: 30px;
}

.stat-item {
    text-align: center;
    padding: 10px 15px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
}

.stat-item i {
    display: block;
    font-size: 1.5rem;
    color: var(--neon-cyan);
    margin-bottom: 5px;
}

.stat-label {
    display: block;
    font-size: 0.7rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.stat-value {
    display: block;
    font-family: var(--font-primary);
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-top: 3px;
}

/* Controles del header */
.header-controls {
    display: flex;
    gap: 10px;
}

.icon-btn {
    width: 50px;
    height: 50px;
    border: none;
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    border-radius: 15px;
    cursor: pointer;
    transition: all var(--transition-smooth);
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.icon-btn:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
}

.icon-btn i {
    font-size: 1.2rem;
}

/* Contenedor principal del juego */
.game-container {
    display: grid;
    grid-template-columns: 350px 1fr 350px;
    gap: 20px;
    padding: 20px;
    max-width: 1600px;
    margin: 0 auto;
    min-height: calc(100vh - 120px);
}

/* Paneles laterales */
.control-panel,
.stats-panel {
    background: rgba(26, 26, 46, 0.8);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    height: fit-content;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

/* Secciones de paneles */
.panel-section {
    margin-bottom: 30px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.section-title {
    font-family: var(--font-primary);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.section-title i {
    color: var(--neon-cyan);
    font-size: 1.3rem;
}

/* Selector de algoritmos */
.algorithm-selector {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.algorithm-option {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    border: 2px solid transparent;
    cursor: pointer;
    transition: all var(--transition-smooth);
    position: relative;
    overflow: hidden;
}

.algorithm-option::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent 0%, rgba(0, 255, 255, 0.1) 50%, transparent 100%);
    transition: left 0.5s ease;
}

.algorithm-option:hover::before {
    left: 100%;
}

.algorithm-option:hover {
    transform: translateX(5px);
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(0, 255, 255, 0.3);
}

.algorithm-option.active {
    background: rgba(0, 255, 255, 0.1);
    border-color: var(--neon-cyan);
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
}

.algo-icon {
    width: 40px;
    height: 40px;
    background: var(--gradient-cyber);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.algo-icon i {
    color: white;
    font-size: 1.2rem;
}

.algo-info {
    flex: 1;
}

.algo-name {
    display: block;
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.95rem;
}

.algo-desc {
    display: block;
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-top: 3px;
}

.algo-stats {
    text-align: right;
}

.performance {
    font-family: var(--font-primary);
    font-weight: 700;
    font-size: 1.1rem;
    color: var(--neon-green);
}

/* Personalización */
.customization-group {
    margin-bottom: 25px;
}

.custom-label {
    display: block;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 12px;
    font-size: 0.9rem;
}

/* Selector de skins */
.skin-selector {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.skin-option {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 12px 8px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    border: 2px solid transparent;
    cursor: pointer;
    transition: all var(--transition-smooth);
}

.skin-option:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-2px);
}

.skin-option.active {
    border-color: var(--neon-purple);
    background: rgba(138, 43, 226, 0.2);
    box-shadow: 0 0 15px rgba(138, 43, 226, 0.3);
}

.skin-preview {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    position: relative;
}

/* Skins específicas */
.cyber-preview {
    background: linear-gradient(45deg, #00ffff, #0080ff);
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

.neon-preview {
    background: linear-gradient(45deg, #39ff14, #00ff80);
    box-shadow: 0 0 10px rgba(57, 255, 20, 0.5);
}

.matrix-preview {
    background: linear-gradient(45deg, #00ff00, #008000);
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
}

.plasma-preview {
    background: linear-gradient(45deg, #ff1493, #ff69b4);
    box-shadow: 0 0 10px rgba(255, 20, 147, 0.5);
}

.hologram-preview {
    background: linear-gradient(45deg, #87ceeb, #4169e1);
    box-shadow: 0 0 10px rgba(135, 206, 235, 0.5);
}

.quantum-preview {
    background: linear-gradient(45deg, #9370db, #8a2be2);
    box-shadow: 0 0 10px rgba(147, 112, 219, 0.5);
}

.skin-option span {
    font-size: 0.75rem;
    color: var(--text-secondary);
    text-align: center;
}

/* Selector de comida */
.food-selector {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
}

.food-option {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    border: 2px solid transparent;
    cursor: pointer;
    transition: all var(--transition-smooth);
}

.food-option:hover {
    background: rgba(255, 255, 255, 0.1);
}

.food-option.active {
    border-color: var(--neon-orange);
    background: rgba(255, 102, 0, 0.2);
}

.food-preview {
    width: 20px;
    height: 20px;
    border-radius: 4px;
}

.energy-preview {
    background: radial-gradient(circle, #ffff00, #ff8c00);
    box-shadow: 0 0 8px rgba(255, 255, 0, 0.6);
}

.crystal-preview {
    background: radial-gradient(circle, #00ffff, #0080ff);
    box-shadow: 0 0 8px rgba(0, 255, 255, 0.6);
}

.orb-preview {
    background: radial-gradient(circle, #ff10f0, #8a2be2);
    box-shadow: 0 0 8px rgba(255, 16, 240, 0.6);
}

.data-preview {
    background: radial-gradient(circle, #39ff14, #00ff80);
    box-shadow: 0 0 8px rgba(57, 255, 20, 0.6);
}

/* Controles de efectos */
.effects-controls {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
}

.effect-toggle {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    border: 2px solid transparent;
    cursor: pointer;
    transition: all var(--transition-smooth);
    font-size: 0.8rem;
}

.effect-toggle:hover {
    background: rgba(255, 255, 255, 0.1);
}

.effect-toggle.active {
    border-color: var(--neon-green);
    background: rgba(57, 255, 20, 0.2);
}

.effect-toggle i {
    color: var(--neon-green);
}

/* Controles principales */
.main-controls {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 25px;
}

.play-button {
    position: relative;
    width: 100%;
    height: 60px;
    border: none;
    background: var(--gradient-cyber);
    color: var(--text-primary);
    font-family: var(--font-primary);
    font-size: 1.1rem;
    font-weight: 700;
    text-transform: uppercase;
    border-radius: 15px;
    cursor: pointer;
    overflow: hidden;
    transition: all var(--transition-smooth);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    letter-spacing: 0.1em;
}

.play-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 255, 255, 0.4);
}

.button-glow {
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.4) 50%, transparent 100%);
    transition: left 0.6s ease;
}

.play-button:hover .button-glow {
    left: 100%;
}

.secondary-controls {
    display: flex;
    gap: 10px;
    justify-content: space-between;
}

.control-btn {
    flex: 1;
    height: 45px;
    border: none;
    background: rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    border-radius: 10px;
    cursor: pointer;
    transition: all var(--transition-smooth);
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.control-btn:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
}

.control-btn i {
    font-size: 1.1rem;
}

/* Control de velocidad */
.speed-control {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.slider-container {
    position: relative;
    margin: 10px 0;
}

.custom-slider {
    width: 100%;
    height: 6px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    outline: none;
    appearance: none;
    cursor: pointer;
}

.custom-slider::-webkit-slider-thumb {
    appearance: none;
    width: 20px;
    height: 20px;
    background: var(--gradient-cyber);
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

.custom-slider::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: var(--gradient-cyber);
    border-radius: 50%;
    cursor: pointer;
    border: none;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

.speed-indicators {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
    font-size: 0.7rem;
    color: var(--text-secondary);
}

.speed-display {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    margin-top: 10px;
}

.speed-display #speed-value {
    font-family: var(--font-primary);
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--neon-cyan);
}

.unit {
    font-size: 0.8rem;
    color: var(--text-secondary);
}

/* Área de juego */
.game-area {
    display: flex;
    align-items: center;
    justify-content: center;
}

.game-viewport {
    position: relative;
    width: 800px;
    height: 800px;
    background: radial-gradient(circle at center, rgba(26, 26, 46, 0.9) 0%, rgba(10, 10, 15, 0.95) 100%);
    border-radius: 20px;
    border: 3px solid var(--neon-cyan);
    box-shadow: 
        0 0 50px rgba(0, 255, 255, 0.3),
        inset 0 0 50px rgba(0, 0, 0, 0.3);
    overflow: hidden;
}

#game-canvas {
    width: 100%;
    height: 100%;
    display: block;
}

/* Efectos del canvas */
#canvas-effects {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}

.effect-layer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

/* HUD del juego */
.game-hud {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 10;
}

.hud-corner {
    position: absolute;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 15px;
}

.top-left { top: 20px; left: 20px; }
.top-right { top: 20px; right: 20px; }
.bottom-left { bottom: 20px; left: 20px; }
.bottom-right { bottom: 20px; right: 20px; }

.hud-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.9rem;
}

.hud-item i {
    color: var(--neon-cyan);
    font-size: 1.1rem;
}

.hud-label {
    color: var(--text-secondary);
    text-transform: uppercase;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
}

.hud-value {
    font-family: var(--font-primary);
    font-weight: 700;
    color: var(--text-primary);
    font-size: 1.1rem;
}

.hud-max {
    color: var(--text-secondary);
    font-size: 0.9rem;
}

/* Indicadores de progreso */
.progress-indicators {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 300px;
}

.progress-bar {
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 25px;
    padding: 10px 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.progress-label {
    display: block;
    font-size: 0.7rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 5px;
}

.progress-track {
    width: 100%;
    height: 8px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 5px;
}

.progress-fill {
    height: 100%;
    background: var(--gradient-neon);
    border-radius: 10px;
    width: 0%;
    transition: width 0.3s ease;
    position: relative;
}

.progress-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.3) 50%, transparent 100%);
    animation: progressShine 2s linear infinite;
}

@keyframes progressShine {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.progress-text {
    font-family: var(--font-primary);
    font-size: 0.8rem;
    color: var(--text-primary);
    text-align: center;
}

/* Panel de estadísticas */
.stats-grid {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.stat-card {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all var(--transition-smooth);
}

.stat-card:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateX(3px);
}

.stat-card .stat-icon {
    width: 40px;
    height: 40px;
    background: var(--gradient-neon);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.stat-card .stat-icon i {
    color: white;
    font-size: 1.1rem;
}

.stat-card .stat-info {
    flex: 1;
}

.stat-card .stat-label {
    display: block;
    font-size: 0.8rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.stat-card .stat-value {
    font-family: var(--font-primary);
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-top: 2px;
}

.stat-card .stat-unit {
    font-size: 0.7rem;
    color: var(--text-secondary);
    margin-left: 3px;
}

/* Indicadores especiales */
.stat-trend,
.stat-indicator,
.efficiency-bar {
    width: 40px;
    height: 20px;
    flex-shrink: 0;
}

.mini-chart {
    width: 100%;
    height: 100%;
    border-radius: 4px;
}

.stat-indicator {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    overflow: hidden;
    position: relative;
}

.efficiency-bar {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    overflow: hidden;
    position: relative;
}

.efficiency-fill {
    height: 100%;
    background: var(--gradient-neon);
    width: 100%;
    border-radius: 10px;
    transition: width 0.3s ease;
}

/* Gráfico de rendimiento */
.chart-container {
    position: relative;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

#performance-chart {
    width: 100%;
    height: 150px;
    border-radius: 8px;
}

.chart-legend {
    display: flex;
    gap: 15px;
    margin-top: 10px;
    justify-content: center;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 0.75rem;
    color: var(--text-secondary);
}

.legend-color {
    width: 12px;
    height: 12px;
    border-radius: 2px;
}

.search-time { background: var(--neon-cyan); }
.nodes-count { background: var(--neon-purple); }

/* Propuesta de valor */
.value-content {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.value-item {
    display: flex;
    gap: 15px;
    align-items: flex-start;
    padding: 15px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    border-left: 4px solid var(--neon-cyan);
}

.value-icon {
    width: 40px;
    height: 40px;
    background: var(--gradient-cyber);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.value-icon i {
    color: white;
    font-size: 1.1rem;
}

.value-text strong {
    display: block;
    color: var(--text-primary);
    margin-bottom: 5px;
    font-size: 0.9rem;
}

.value-text p {
    color: var(--text-secondary);
    font-size: 0.8rem;
    line-height: 1.4;
}

/* Modales */
.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    animation: modalFadeIn 0.3s ease;
}

@keyframes modalFadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

.modal.show {
    display: flex;
}

.modal-content {
    background: var(--gradient-primary);
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    border: 2px solid var(--neon-cyan);
    box-shadow: 0 0 50px rgba(0, 255, 255, 0.5);
    transform: scale(0.9);
    animation: modalScale 0.3s ease forwards;
}

@keyframes modalScale {
    0% { transform: scale(0.9); }
    100% { transform: scale(1); }
}

/* Modal de victoria */
.victory-animation {
    font-size: 5rem;
    color: var(--neon-yellow);
    margin-bottom: 20px;
    animation: victoryBounce 2s ease-in-out infinite;
}

@keyframes victoryBounce {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(10deg); }
}

.victory-content h2 {
    font-family: var(--font-primary);
    font-size: 2.5rem;
    margin-bottom: 30px;
    background: var(--gradient-neon);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.victory-stats {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 30px;
    padding: 20px;
    background: rgba(0, 0, 0, 0.3);
    border-radius: 15px;
}

.victory-stat {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.victory-stat:last-child {
    border-bottom: none;
}

.victory-button {
    background: var(--gradient-cyber);
    border: none;
    padding: 15px 30px;
    border-radius: 25px;
    color: var(--text-primary);
    font-family: var(--font-primary);
    font-weight: 700;
    font-size: 1.1rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all var(--transition-smooth);
}

.victory-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 255, 255, 0.4);
}

/* Modal de game over */
.gameover-animation {
    font-size: 4rem;
    color: var(--text-error);
    margin-bottom: 20px;
    animation: gameoverShake 0.5s ease-in-out 3;
}

@keyframes gameoverShake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

.gameover-content h2 {
    font-family: var(--font-primary);
    font-size: 2rem;
    margin-bottom: 30px;
    color: var(--text-primary);
}

.gameover-analysis {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 30px;
}

.gameover-analysis h3 {
    color: var(--text-accent);
    margin-bottom: 15px;
    font-size: 1.2rem;
}

.analysis-grid {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.analysis-item {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.analysis-item:last-child {
    border-bottom: none;
}

.gameover-button {
    background: linear-gradient(135deg, var(--text-error), #cc1f1f);
    border: none;
    padding: 15px 30px;
    border-radius: 25px;
    color: var(--text-primary);
    font-family: var(--font-primary);
    font-weight: 700;
    font-size: 1.1rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all var(--transition-smooth);
}

.gameover-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(239, 68, 68, 0.4);
}

/* Efectos especiales en el juego */
#special-effects {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 5;
}

.effect-burst,
.effect-explosion,
.effect-aura {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}

/* Animaciones de entrada */
@keyframes slideInFromLeft {
    0% { transform: translateX(-100%); opacity: 0; }
    100% { transform: translateX(0); opacity: 1; }
}

@keyframes slideInFromRight {
    0% { transform: translateX(100%); opacity: 0; }
    100% { transform: translateX(0); opacity: 1; }
}

@keyframes slideInFromTop {
    0% { transform: translateY(-100%); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
}

@keyframes slideInFromBottom {
    0% { transform: translateY(100%); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
}

/* Aplicar animaciones de entrada */
.control-panel {
    animation: slideInFromLeft 0.8s ease-out;
}

.stats-panel {
    animation: slideInFromRight 0.8s ease-out;
}

.game-area {
    animation: slideInFromTop 0.8s ease-out 0.2s both;
}

.game-header {
    animation: slideInFromTop 0.6s ease-out;
}

/* Responsive */
@media (max-width: 1600px) {
    .game-container {
        grid-template-columns: 320px 1fr 320px;
        gap: 15px;
        padding: 15px;
    }
    
    .game-viewport {
        width: 600px;
        height: 600px;
    }
}

@media (max-width: 1200px) {
    .game-container {
        grid-template-columns: 1fr;
        grid-template-rows: auto 1fr auto;
    }
    
    .control-panel,
    .stats-panel {
        max-height: 400px;
        overflow-y: auto;
    }
    
    .stats-panel {
        order: 3;
    }
    
    .game-area {
        order: 2;
    }
    
    .control-panel {
        order: 1;
    }
}

@media (max-width: 800px) {
    .header-content {
        flex-direction: column;
        gap: 20px;
        text-align: center;
    }
    
    .game-viewport {
        width: 400px;
        height: 400px;
    }
    
    .hud-corner {
        position: static;
        margin-bottom: 10px;
    }
    
    .game-hud {
        position: relative;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        padding: 10px;
    }
    
    .progress-indicators {
        position: static;
        transform: none;
        width: 100%;
        margin-top: 10px;
    }
}

/* Scrollbars personalizados */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: var(--gradient-cyber);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--gradient-neon);
}

/* Utilidades */
.hidden {
    display: none !important;
}

.fade-in {
    animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

.pulse {
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

.glow {
    filter: drop-shadow(0 0 10px currentColor);
}

.text-glow {
    text-shadow: 0 0 10px currentColor;
}

/* Fin del CSS */
'''

# Guardar CSS
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ 2/5 - styles.css creado (Estilos videojuego AAA)")
print("    🎨 Gradientes y efectos neón espectaculares")
print("    ✨ Animaciones fluidas y transiciones suaves")
print("    🌟 Efectos de partículas y resplandor")
print("    🎭 Tema futurista cyberpunk completo")
print("    📱 Diseño completamente responsivo")