// ✨ VISUAL EFFECTS SYSTEM - EFECTOS VIDEOJUEGO AAA
// Sistema de efectos visuales de nivel profesional para Snake AI

class VisualEffectsManager {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;
        this.effects = [];
        this.particles = [];
        this.trails = [];
        this.screenShake = { intensity: 0, duration: 0 };
        this.postProcessing = {
            bloom: true,
            glow: true,
            scanlines: true,
            chromatic: false
        };

        // Configuración de efectos
        this.config = {
            maxParticles: 500,
            maxTrails: 100,
            bloomIntensity: 0.3,
            glowRadius: 20,
            particleLifetime: 2000,
            trailLifetime: 1500
        };

        console.log('✨ Visual Effects Manager inicializado');
        this.initializeShaders();
    }

    initializeShaders() {
        // Inicializar efectos de post-procesamiento
        this.shaders = {
            bloom: this.createBloomEffect(),
            glow: this.createGlowEffect(),
            scanlines: this.createScanlinesEffect(),
            chromatic: this.createChromaticAberration()
        };
    }

    // SISTEMA DE PARTÍCULAS AVANZADO
    createParticleExplosion(x, y, type = 'default', intensity = 1) {
        const particleCount = Math.floor(15 * intensity);
        const colors = this.getParticleColors(type);
        const shapes = this.getParticleShapes(type);

        for (let i = 0; i < particleCount; i++) {
            const angle = (Math.PI * 2 * i) / particleCount + (Math.random() - 0.5) * 0.5;
            const velocity = 2 + Math.random() * 6;
            const size = 2 + Math.random() * 8;
            const life = this.config.particleLifetime * (0.8 + Math.random() * 0.4);

            this.particles.push({
                id: this.generateId(),
                x: x,
                y: y,
                vx: Math.cos(angle) * velocity,
                vy: Math.sin(angle) * velocity,
                size: size,
                originalSize: size,
                life: life,
                maxLife: life,
                color: colors[Math.floor(Math.random() * colors.length)],
                shape: shapes[Math.floor(Math.random() * shapes.length)],
                rotation: Math.random() * Math.PI * 2,
                rotationSpeed: (Math.random() - 0.5) * 0.3,
                gravity: type === 'success' ? 0.1 : 0.2,
                bounce: type === 'energy' ? 0.7 : 0.3,
                glow: type === 'magic' || type === 'energy',
                type: type
            });
        }

        this.limitParticles();
    }

    createTrailEffect(x, y, color = '#8a2be2', intensity = 1) {
        this.trails.push({
            id: this.generateId(),
            x: x,
            y: y,
            color: color,
            life: this.config.trailLifetime * intensity,
            maxLife: this.config.trailLifetime * intensity,
            size: 20 * intensity,
            originalSize: 20 * intensity,
            fadeRate: 1 / (this.config.trailLifetime * intensity)
        });

        this.limitTrails();
    }

    createScreenShake(intensity = 5, duration = 300) {
        this.screenShake.intensity = Math.max(this.screenShake.intensity, intensity);
        this.screenShake.duration = Math.max(this.screenShake.duration, duration);
    }

    createRippleEffect(x, y, color = '#00ffff', maxRadius = 100) {
        this.effects.push({
            type: 'ripple',
            id: this.generateId(),
            x: x,
            y: y,
            color: color,
            radius: 0,
            maxRadius: maxRadius,
            thickness: 3,
            life: 1000,
            maxLife: 1000,
            alpha: 1
        });
    }

    createLightningEffect(startX, startY, endX, endY, color = '#ffff00') {
        const segments = [];
        const distance = Math.sqrt((endX - startX) ** 2 + (endY - startY) ** 2);
        const segmentCount = Math.floor(distance / 10) + 2;

        for (let i = 0; i <= segmentCount; i++) {
            const t = i / segmentCount;
            const x = startX + (endX - startX) * t + (Math.random() - 0.5) * 20 * (1 - Math.abs(t - 0.5) * 2);
            const y = startY + (endY - startY) * t + (Math.random() - 0.5) * 20 * (1 - Math.abs(t - 0.5) * 2);

            segments.push({ x, y });
        }

        // Asegurar que empiece y termine en los puntos exactos
        segments[0] = { x: startX, y: startY };
        segments[segments.length - 1] = { x: endX, y: endY };

        this.effects.push({
            type: 'lightning',
            id: this.generateId(),
            segments: segments,
            color: color,
            thickness: 3,
            life: 200,
            maxLife: 200,
            alpha: 1,
            flicker: true
        });
    }

    createWaveEffect(centerX, centerY, color = '#00ffff') {
        for (let i = 0; i < 3; i++) {
            setTimeout(() => {
                this.effects.push({
                    type: 'wave',
                    id: this.generateId(),
                    x: centerX,
                    y: centerY,
                    color: color,
                    radius: 0,
                    maxRadius: 80 + i * 20,
                    thickness: 2,
                    speed: 2 + i * 0.5,
                    life: 800,
                    maxLife: 800,
                    alpha: 0.8 - i * 0.2
                });
            }, i * 100);
        }
    }

    // ACTUALIZACIÓN DE EFECTOS
    update(deltaTime) {
        this.updateParticles(deltaTime);
        this.updateTrails(deltaTime);
        this.updateEffects(deltaTime);
        this.updateScreenShake(deltaTime);
    }

    updateParticles(deltaTime) {
        this.particles = this.particles.filter(particle => {
            // Actualizar posición
            particle.x += particle.vx;
            particle.y += particle.vy;

            // Aplicar gravedad
            particle.vy += particle.gravity;

            // Fricción del aire
            particle.vx *= 0.98;
            particle.vy *= 0.98;

            // Rebote en bordes (opcional)
            if (particle.bounce > 0) {
                if (particle.x <= 0 || particle.x >= this.canvas.width) {
                    particle.vx *= -particle.bounce;
                    particle.x = Math.max(0, Math.min(this.canvas.width, particle.x));
                }
                if (particle.y <= 0 || particle.y >= this.canvas.height) {
                    particle.vy *= -particle.bounce;
                    particle.y = Math.max(0, Math.min(this.canvas.height, particle.y));
                }
            }

            // Actualizar rotación
            particle.rotation += particle.rotationSpeed;

            // Actualizar vida
            particle.life -= deltaTime;
            const lifeRatio = particle.life / particle.maxLife;

            // Actualizar tamaño (fade out)
            particle.size = particle.originalSize * lifeRatio;

            return particle.life > 0;
        });
    }

    updateTrails(deltaTime) {
        this.trails = this.trails.filter(trail => {
            trail.life -= deltaTime;
            const lifeRatio = trail.life / trail.maxLife;

            trail.size = trail.originalSize * lifeRatio;

            return trail.life > 0;
        });
    }

    updateEffects(deltaTime) {
        this.effects = this.effects.filter(effect => {
            effect.life -= deltaTime;
            const lifeRatio = effect.life / effect.maxLife;

            switch (effect.type) {
                case 'ripple':
                    effect.radius += (effect.maxRadius / effect.maxLife) * deltaTime;
                    effect.alpha = lifeRatio;
                    break;

                case 'wave':
                    effect.radius += effect.speed;
                    effect.alpha = lifeRatio * 0.8;
                    break;

                case 'lightning':
                    effect.alpha = effect.flicker ? (Math.random() > 0.3 ? lifeRatio : 0) : lifeRatio;
                    break;
            }

            return effect.life > 0;
        });
    }

    updateScreenShake(deltaTime) {
        if (this.screenShake.duration > 0) {
            this.screenShake.duration -= deltaTime;
            this.screenShake.intensity *= 0.95; // Decay

            if (this.screenShake.duration <= 0) {
                this.screenShake.intensity = 0;
            }
        }
    }

    // RENDERIZADO DE EFECTOS
    render() {
        if (this.screenShake.intensity > 0) {
            this.applyScreenShake();
        }

        this.renderTrails();
        this.renderEffects();
        this.renderParticles();

        if (this.postProcessing.scanlines) {
            this.renderScanlines();
        }
    }

    renderParticles() {
        this.particles.forEach(particle => {
            const alpha = particle.life / particle.maxLife;
            this.ctx.save();

            // Posicionar y rotar
            this.ctx.translate(particle.x, particle.y);
            this.ctx.rotate(particle.rotation);

            // Aplicar glow si corresponde
            if (particle.glow) {
                this.ctx.shadowColor = particle.color;
                this.ctx.shadowBlur = particle.size * 2;
            }

            // Renderizar según forma
            this.renderParticleShape(particle, alpha);

            this.ctx.restore();
        });
    }

    renderParticleShape(particle, alpha) {
        const color = this.addAlphaToColor(particle.color, alpha);
        this.ctx.fillStyle = color;

        switch (particle.shape) {
            case 'circle':
                this.ctx.beginPath();
                this.ctx.arc(0, 0, particle.size, 0, Math.PI * 2);
                this.ctx.fill();
                break;

            case 'square':
                this.ctx.fillRect(-particle.size/2, -particle.size/2, particle.size, particle.size);
                break;

            case 'diamond':
                this.ctx.beginPath();
                this.ctx.moveTo(0, -particle.size);
                this.ctx.lineTo(particle.size, 0);
                this.ctx.lineTo(0, particle.size);
                this.ctx.lineTo(-particle.size, 0);
                this.ctx.closePath();
                this.ctx.fill();
                break;

            case 'star':
                this.renderStar(0, 0, particle.size, 5);
                break;

            case 'spark':
                this.renderSpark(0, 0, particle.size);
                break;
        }
    }

    renderTrails() {
        this.trails.forEach(trail => {
            const alpha = trail.life / trail.maxLife;
            const color = this.addAlphaToColor(trail.color, alpha * 0.6);

            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(trail.x, trail.y, trail.size, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }

    renderEffects() {
        this.effects.forEach(effect => {
            this.ctx.save();

            switch (effect.type) {
                case 'ripple':
                    this.renderRipple(effect);
                    break;
                case 'wave':
                    this.renderWave(effect);
                    break;
                case 'lightning':
                    this.renderLightning(effect);
                    break;
            }

            this.ctx.restore();
        });
    }

    renderRipple(effect) {
        const color = this.addAlphaToColor(effect.color, effect.alpha);

        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = effect.thickness;
        this.ctx.beginPath();
        this.ctx.arc(effect.x, effect.y, effect.radius, 0, Math.PI * 2);
        this.ctx.stroke();
    }

    renderWave(effect) {
        const color = this.addAlphaToColor(effect.color, effect.alpha);

        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = effect.thickness;
        this.ctx.beginPath();
        this.ctx.arc(effect.x, effect.y, effect.radius, 0, Math.PI * 2);
        this.ctx.stroke();
    }

    renderLightning(effect) {
        if (effect.alpha <= 0) return;

        const color = this.addAlphaToColor(effect.color, effect.alpha);

        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = effect.thickness;
        this.ctx.lineCap = 'round';
        this.ctx.lineJoin = 'round';

        // Glow effect
        this.ctx.shadowColor = effect.color;
        this.ctx.shadowBlur = 10;

        this.ctx.beginPath();
        effect.segments.forEach((segment, i) => {
            if (i === 0) {
                this.ctx.moveTo(segment.x, segment.y);
            } else {
                this.ctx.lineTo(segment.x, segment.y);
            }
        });
        this.ctx.stroke();
    }

    renderStar(x, y, size, points) {
        const outerRadius = size;
        const innerRadius = size * 0.4;

        this.ctx.beginPath();
        for (let i = 0; i < points * 2; i++) {
            const angle = (i * Math.PI) / points;
            const radius = i % 2 === 0 ? outerRadius : innerRadius;
            const px = x + Math.cos(angle) * radius;
            const py = y + Math.sin(angle) * radius;

            if (i === 0) {
                this.ctx.moveTo(px, py);
            } else {
                this.ctx.lineTo(px, py);
            }
        }
        this.ctx.closePath();
        this.ctx.fill();
    }

    renderSpark(x, y, size) {
        const length = size * 2;

        this.ctx.strokeStyle = this.ctx.fillStyle;
        this.ctx.lineWidth = size / 4;
        this.ctx.lineCap = 'round';

        // Línea horizontal
        this.ctx.beginPath();
        this.ctx.moveTo(x - length/2, y);
        this.ctx.lineTo(x + length/2, y);
        this.ctx.stroke();

        // Línea vertical
        this.ctx.beginPath();
        this.ctx.moveTo(x, y - length/2);
        this.ctx.lineTo(x, y + length/2);
        this.ctx.stroke();
    }

    renderScanlines() {
        const lineSpacing = 4;

        this.ctx.save();
        this.ctx.globalAlpha = 0.1;
        this.ctx.strokeStyle = '#00ffff';
        this.ctx.lineWidth = 1;

        for (let y = 0; y < this.canvas.height; y += lineSpacing) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.canvas.width, y);
            this.ctx.stroke();
        }

        this.ctx.restore();
    }

    applyScreenShake() {
        const shakeX = (Math.random() - 0.5) * this.screenShake.intensity;
        const shakeY = (Math.random() - 0.5) * this.screenShake.intensity;

        this.ctx.translate(shakeX, shakeY);
    }

    // POST-PROCESSING EFFECTS
    createBloomEffect() {
        return {
            intensity: this.config.bloomIntensity,
            threshold: 0.7,
            apply: (imageData) => {
                // Implementación simplificada de bloom
                return imageData;
            }
        };
    }

    createGlowEffect() {
        return {
            radius: this.config.glowRadius,
            intensity: 0.5,
            apply: (x, y, color, size) => {
                const gradient = this.ctx.createRadialGradient(x, y, 0, x, y, size + this.config.glowRadius);
                gradient.addColorStop(0, color);
                gradient.addColorStop(1, this.addAlphaToColor(color, 0));
                return gradient;
            }
        };
    }

    createScanlinesEffect() {
        return {
            spacing: 4,
            opacity: 0.1,
            color: '#00ffff'
        };
    }

    createChromaticAberration() {
        return {
            intensity: 2,
            apply: (imageData) => {
                // Implementación simplificada de aberración cromática
                return imageData;
            }
        };
    }

    // UTILIDADES
    getParticleColors(type) {
        const colorSets = {
            success: ['#39ff14', '#00ffff', '#ffff00', '#00ff80'],
            collision: ['#ff0000', '#ff6600', '#ffff00', '#ff1493'],
            energy: ['#ffff00', '#ff8c00', '#ffffff', '#ffd700'],
            magic: ['#ff10f0', '#8a2be2', '#9370db', '#dda0dd'],
            ice: ['#00ffff', '#87ceeb', '#b0e0e6', '#e0ffff'],
            fire: ['#ff4500', '#ff6347', '#ffa500', '#ffff00'],
            electric: ['#ffff00', '#00ffff', '#ffffff', '#9aff9a']
        };

        return colorSets[type] || colorSets.success;
    }

    getParticleShapes(type) {
        const shapeSets = {
            success: ['circle', 'star'],
            collision: ['circle', 'square', 'diamond'],
            energy: ['circle', 'spark', 'star'],
            magic: ['diamond', 'star', 'circle'],
            ice: ['diamond', 'circle'],
            fire: ['circle', 'spark'],
            electric: ['spark', 'star']
        };

        return shapeSets[type] || ['circle'];
    }

    addAlphaToColor(color, alpha) {
        // Convertir color hex a rgba
        if (color.startsWith('#')) {
            const hex = color.slice(1);
            const r = parseInt(hex.substr(0, 2), 16);
            const g = parseInt(hex.substr(2, 2), 16);
            const b = parseInt(hex.substr(4, 2), 16);
            return `rgba(${r}, ${g}, ${b}, ${alpha})`;
        }

        // Si ya es rgba, modificar alpha
        if (color.startsWith('rgba')) {
            return color.replace(/[\d.]+(?=\))/, alpha.toString());
        }

        // Si es rgb, convertir a rgba
        if (color.startsWith('rgb')) {
            return color.replace('rgb', 'rgba').replace(')', `, ${alpha})`);
        }

        return color;
    }

    generateId() {
        return Math.random().toString(36).substr(2, 9);
    }

    limitParticles() {
        if (this.particles.length > this.config.maxParticles) {
            this.particles.splice(0, this.particles.length - this.config.maxParticles);
        }
    }

    limitTrails() {
        if (this.trails.length > this.config.maxTrails) {
            this.trails.splice(0, this.trails.length - this.config.maxTrails);
        }
    }

    // MÉTODOS PÚBLICOS DE CONTROL
    setPostProcessing(effect, enabled) {
        if (this.postProcessing.hasOwnProperty(effect)) {
            this.postProcessing[effect] = enabled;
        }
    }

    clearAllEffects() {
        this.particles = [];
        this.trails = [];
        this.effects = [];
        this.screenShake = { intensity: 0, duration: 0 };
    }

    getEffectsCount() {
        return {
            particles: this.particles.length,
            trails: this.trails.length,
            effects: this.effects.length,
            total: this.particles.length + this.trails.length + this.effects.length
        };
    }

    setConfig(key, value) {
        if (this.config.hasOwnProperty(key)) {
            this.config[key] = value;
        }
    }
}

// MANAGER DE AUDIO AVANZADO
class AudioManager {
    constructor() {
        this.audioContext = null;
        this.enabled = true;
        this.volume = 0.7;
        this.sounds = {};

        this.initializeAudio();
    }

    initializeAudio() {
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.generateSounds();
            console.log('🔊 Audio Manager inicializado');
        } catch (e) {
            console.log('⚠️ Audio no disponible:', e);
            this.enabled = false;
        }
    }

    generateSounds() {
        this.sounds = {
            collect: { frequencies: [440, 523, 659], duration: 0.3, type: 'success' },
            collision: { frequencies: [220, 165, 110], duration: 0.8, type: 'error' },
            victory: { frequencies: [523, 659, 784, 1047], duration: 1.2, type: 'victory' },
            move: { frequencies: [330], duration: 0.1, type: 'action' },
            pause: { frequencies: [440, 330], duration: 0.4, type: 'ui' }
        };
    }

    playSound(soundName) {
        if (!this.enabled || !this.audioContext || !this.sounds[soundName]) {
            return;
        }

        const sound = this.sounds[soundName];
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);

        // Configurar frecuencias
        if (sound.frequencies.length === 1) {
            oscillator.frequency.setValueAtTime(sound.frequencies[0], this.audioContext.currentTime);
        } else {
            sound.frequencies.forEach((freq, index) => {
                const time = this.audioContext.currentTime + (index * sound.duration / sound.frequencies.length);
                oscillator.frequency.setValueAtTime(freq, time);
            });
        }

        // Configurar volumen y envelope
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.linearRampToValueAtTime(this.volume * 0.1, this.audioContext.currentTime + 0.01);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + sound.duration);

        // Tipo de onda según el sonido
        const waveTypes = {
            success: 'sine',
            error: 'sawtooth',
            victory: 'square',
            action: 'triangle',
            ui: 'sine'
        };

        oscillator.type = waveTypes[sound.type] || 'sine';

        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + sound.duration);
    }

    setVolume(volume) {
        this.volume = Math.max(0, Math.min(1, volume));
    }

    toggleAudio() {
        this.enabled = !this.enabled;
        return this.enabled;
    }
}

// MANAGER DE ANIMACIONES SUAVES
class AnimationManager {
    constructor() {
        this.animations = [];
        this.easingFunctions = {
            linear: t => t,
            easeIn: t => t * t,
            easeOut: t => t * (2 - t),
            easeInOut: t => t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t,
            bounce: t => {
                if (t < 1/2.75) return 7.5625 * t * t;
                else if (t < 2/2.75) return 7.5625 * (t -= 1.5/2.75) * t + 0.75;
                else if (t < 2.5/2.75) return 7.5625 * (t -= 2.25/2.75) * t + 0.9375;
                else return 7.5625 * (t -= 2.625/2.75) * t + 0.984375;
            }
        };
    }

    animate(options) {
        const animation = {
            id: this.generateId(),
            startTime: performance.now(),
            duration: options.duration || 1000,
            from: options.from || 0,
            to: options.to || 1,
            easing: this.easingFunctions[options.easing] || this.easingFunctions.linear,
            onUpdate: options.onUpdate || (() => {}),
            onComplete: options.onComplete || (() => {}),
            target: options.target
        };

        this.animations.push(animation);
        return animation.id;
    }

    update() {
        const currentTime = performance.now();

        this.animations = this.animations.filter(animation => {
            const elapsed = currentTime - animation.startTime;
            const progress = Math.min(elapsed / animation.duration, 1);
            const easedProgress = animation.easing(progress);

            const currentValue = animation.from + (animation.to - animation.from) * easedProgress;
            animation.onUpdate(currentValue, animation.target);

            if (progress >= 1) {
                animation.onComplete(animation.target);
                return false;
            }

            return true;
        });
    }

    stopAnimation(id) {
        const index = this.animations.findIndex(anim => anim.id === id);
        if (index !== -1) {
            this.animations.splice(index, 1);
        }
    }

    generateId() {
        return Math.random().toString(36).substr(2, 9);
    }
}

console.log('✨ Visual Effects System cargado completamente');
console.log('   🎆 Sistema de partículas avanzado');
console.log('   ⚡ Efectos de pantalla (shake, glow, trails)');
console.log('   🌊 Ondas y ondulaciones dinámicas');
console.log('   ⭐ Rayos y efectos de luz');
console.log('   🎵 Audio procedural integrado');
console.log('   🎬 Sistema de animaciones suaves');
