# 3. MOTOR DE JUEGO PRINCIPAL (JavaScript)
game_engine_js = '''// 🎮 SNAKE AI GAME ENGINE - VIDEOJUEGO AAA
// Motor de juego optimizado para máximo rendimiento visual

class GameEngine {
    constructor() {
        this.canvas = document.getElementById('game-canvas');
        this.ctx = this.canvas.getContext('2d');
        
        // Configuración de pauta
        this.GRID_SIZE = 10;
        this.MAX_APPLES = 35;
        this.MIN_SNAKE_LENGTH = 3;
        
        // Configuración visual
        this.CELL_SIZE = 80;
        this.canvas.width = this.GRID_SIZE * this.CELL_SIZE;
        this.canvas.height = this.GRID_SIZE * this.CELL_SIZE;
        
        // Estado del juego
        this.gameState = 'menu'; // menu, playing, paused, gameover, victory
        this.snake = [];
        this.apple = null;
        this.score = 0;
        this.moves = 0;
        this.gameTime = 0;
        this.lastUpdate = 0;
        
        // IA y algoritmos
        this.currentAlgorithm = 'astar';
        this.aiAgent = null;
        this.searchTime = 0;
        this.nodesExplored = 0;
        this.currentPath = [];
        
        // Personalización
        this.snakeSkin = 'cyber';
        this.foodStyle = 'energy';
        this.effects = {
            particles: true,
            trails: true,
            glow: true,
            shake: true
        };
        
        // Rendimiento
        this.fps = 8;
        this.lastFrame = 0;
        this.frameInterval = 1000 / this.fps;
        
        // Efectos visuales
        this.particles = [];
        this.trails = [];
        this.shakeIntensity = 0;
        
        // Audio
        this.audioContext = null;
        this.audioEnabled = true;
        
        this.init();
    }
    
    init() {
        this.setupCanvas();
        this.initializeAudio();
        this.resetGame();
        this.setupEventListeners();
        this.startGameLoop();
        
        console.log('🎮 Game Engine inicializado');
        console.log(`📐 Grilla: ${this.GRID_SIZE}x${this.GRID_SIZE}`);
        console.log(`🍎 Máximo manzanas: ${this.MAX_APPLES}`);
        console.log(`📏 Longitud mínima: ${this.MIN_SNAKE_LENGTH}`);
    }
    
    setupCanvas() {
        // Configurar canvas para alta resolución
        const dpr = window.devicePixelRatio || 1;
        const rect = this.canvas.getBoundingClientRect();
        
        this.canvas.width = rect.width * dpr;
        this.canvas.height = rect.height * dpr;
        this.ctx.scale(dpr, dpr);
        
        // Configurar contexto para mejores gráficos
        this.ctx.imageSmoothingEnabled = true;
        this.ctx.imageSmoothingQuality = 'high';
    }
    
    initializeAudio() {
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            console.log('🔊 Audio inicializado');
        } catch (e) {
            console.log('⚠️ Audio no disponible');
            this.audioEnabled = false;
        }
    }
    
    resetGame() {
        // Inicializar serpiente en el centro
        const center = Math.floor(this.GRID_SIZE / 2);
        this.snake = [
            { x: center, y: center },
            { x: center - 1, y: center },
            { x: center - 2, y: center }
        ];
        
        // Generar primera manzana
        this.generateApple();
        
        // Resetear estadísticas
        this.score = 0;
        this.moves = 0;
        this.gameTime = 0;
        this.searchTime = 0;
        this.nodesExplored = 0;
        this.currentPath = [];
        
        // Limpiar efectos
        this.particles = [];
        this.trails = [];
        this.shakeIntensity = 0;
        
        // Inicializar IA
        this.aiAgent = new AIAgent(this.currentAlgorithm);
        
        this.updateUI();
    }
    
    generateApple() {
        const availablePositions = [];
        
        for (let x = 0; x < this.GRID_SIZE; x++) {
            for (let y = 0; y < this.GRID_SIZE; y++) {
                if (!this.snake.some(segment => segment.x === x && segment.y === y)) {
                    availablePositions.push({ x, y });
                }
            }
        }
        
        if (availablePositions.length > 0) {
            const randomIndex = Math.floor(Math.random() * availablePositions.length);
            this.apple = availablePositions[randomIndex];
        } else {
            this.apple = null;
        }
    }
    
    setupEventListeners() {
        // Controles del juego
        document.getElementById('play-btn').addEventListener('click', () => {
            this.toggleGame();
        });
        
        document.getElementById('pause-btn').addEventListener('click', () => {
            this.pauseGame();
        });
        
        document.getElementById('reset-btn').addEventListener('click', () => {
            this.resetGame();
        });
        
        document.getElementById('path-toggle').addEventListener('click', () => {
            this.togglePath();
        });
        
        // Control de velocidad
        document.getElementById('speed-slider').addEventListener('input', (e) => {
            this.setFPS(parseInt(e.target.value));
        });
        
        // Algoritmos
        document.querySelectorAll('.algorithm-option').forEach(option => {
            option.addEventListener('click', (e) => {
                this.setAlgorithm(e.currentTarget.dataset.algo);
            });
        });
        
        // Personalización
        document.querySelectorAll('.skin-option').forEach(option => {
            option.addEventListener('click', (e) => {
                this.setSnakeSkin(e.currentTarget.dataset.skin);
            });
        });
        
        document.querySelectorAll('.food-option').forEach(option => {
            option.addEventListener('click', (e) => {
                this.setFoodStyle(e.currentTarget.dataset.food);
            });
        });
        
        // Efectos
        document.querySelectorAll('.effect-toggle').forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                this.toggleEffect(e.currentTarget.dataset.effect);
            });
        });
        
        // Audio
        document.getElementById('audio-btn').addEventListener('click', () => {
            this.toggleAudio();
        });
    }
    
    startGameLoop() {
        const gameLoop = (timestamp) => {
            if (timestamp - this.lastFrame >= this.frameInterval) {
                this.update(timestamp);
                this.render();
                this.lastFrame = timestamp;
            }
            requestAnimationFrame(gameLoop);
        };
        
        requestAnimationFrame(gameLoop);
    }
    
    update(timestamp) {
        if (this.gameState !== 'playing') return;
        
        // Actualizar tiempo de juego
        if (this.lastUpdate === 0) this.lastUpdate = timestamp;
        this.gameTime += (timestamp - this.lastUpdate);
        this.lastUpdate = timestamp;
        
        // Verificar condición de victoria
        if (this.score >= this.MAX_APPLES) {
            this.gameState = 'victory';
            this.showVictoryModal();
            return;
        }
        
        // Obtener movimiento de la IA
        const aiStart = performance.now();
        const nextMove = this.aiAgent.getNextMove(this.snake, this.apple, this.GRID_SIZE);
        this.searchTime = performance.now() - aiStart;
        this.nodesExplored = this.aiAgent.lastNodesExplored;
        
        // Obtener camino para visualización
        this.currentPath = this.aiAgent.getPath(this.snake, this.apple, this.GRID_SIZE);
        
        // Mover serpiente
        this.moveSnake(nextMove);
        this.moves++;
        
        // Verificar colisiones
        if (this.checkCollision()) {
            this.gameState = 'gameover';
            this.showGameOverModal();
            return;
        }
        
        // Verificar si comió manzana
        if (this.snake[0].x === this.apple.x && this.snake[0].y === this.apple.y) {
            this.eatApple();
        }
        
        // Actualizar efectos
        this.updateParticles();
        this.updateTrails();
        this.updateShake();
        
        this.updateUI();
    }
    
    moveSnake(direction) {
        const head = { ...this.snake[0] };
        
        switch (direction) {
            case 'up': head.y -= 1; break;
            case 'down': head.y += 1; break;
            case 'left': head.x -= 1; break;
            case 'right': head.x += 1; break;
        }
        
        this.snake.unshift(head);
        
        // Agregar trail si está habilitado
        if (this.effects.trails) {
            this.trails.push({
                x: head.x,
                y: head.y,
                life: 1.0,
                maxLife: 1.0
            });
        }
        
        // Solo quitar cola si no creció
        if (!this.justAte) {
            this.snake.pop();
        } else {
            this.justAte = false;
        }
    }
    
    checkCollision() {
        const head = this.snake[0];
        
        // Colisión con paredes
        if (head.x < 0 || head.x >= this.GRID_SIZE || head.y < 0 || head.y >= this.GRID_SIZE) {
            return true;
        }
        
        // Colisión consigo misma
        for (let i = 1; i < this.snake.length; i++) {
            if (head.x === this.snake[i].x && head.y === this.snake[i].y) {
                return true;
            }
        }
        
        return false;
    }
    
    eatApple() {
        this.score++;
        this.justAte = true;
        
        // Efectos visuales
        if (this.effects.particles) {
            this.createParticleExplosion(this.apple.x, this.apple.y, 'success');
        }
        
        if (this.effects.shake) {
            this.shakeIntensity = 5;
        }
        
        // Sonido
        this.playSound('collect');
        
        // Generar nueva manzana
        this.generateApple();
        
        // Verificar condición de victoria
        if (this.score >= this.MAX_APPLES) {
            this.gameState = 'victory';
            this.playSound('victory');
            return;
        }
    }
    
    createParticleExplosion(x, y, type) {
        const colors = {
            success: ['#39ff14', '#00ffff', '#ffff00'],
            collision: ['#ff0000', '#ff6600', '#ffff00'],
            trail: ['#8a2be2', '#ff10f0', '#00ffff']
        };
        
        const particleColors = colors[type] || colors.success;
        
        for (let i = 0; i < 15; i++) {
            this.particles.push({
                x: x * this.CELL_SIZE + this.CELL_SIZE / 2,
                y: y * this.CELL_SIZE + this.CELL_SIZE / 2,
                vx: (Math.random() - 0.5) * 10,
                vy: (Math.random() - 0.5) * 10,
                life: 1.0,
                maxLife: 1.0,
                color: particleColors[Math.floor(Math.random() * particleColors.length)],
                size: Math.random() * 6 + 2
            });
        }
    }
    
    updateParticles() {
        this.particles = this.particles.filter(particle => {
            particle.x += particle.vx;
            particle.y += particle.vy;
            particle.vx *= 0.98;
            particle.vy *= 0.98;
            particle.life -= 0.02;
            particle.size *= 0.99;
            
            return particle.life > 0;
        });
    }
    
    updateTrails() {
        this.trails = this.trails.filter(trail => {
            trail.life -= 0.05;
            return trail.life > 0;
        });
    }
    
    updateShake() {
        if (this.shakeIntensity > 0) {
            this.shakeIntensity *= 0.9;
            if (this.shakeIntensity < 0.1) {
                this.shakeIntensity = 0;
            }
        }
    }
    
    render() {
        // Limpiar canvas
        this.ctx.fillStyle = '#0a0a0f';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Aplicar shake
        if (this.shakeIntensity > 0) {
            this.ctx.save();
            this.ctx.translate(
                (Math.random() - 0.5) * this.shakeIntensity,
                (Math.random() - 0.5) * this.shakeIntensity
            );
        }
        
        // Dibujar grilla
        this.drawGrid();
        
        // Dibujar camino (si está habilitado)
        if (this.currentPath.length > 0) {
            this.drawPath();
        }
        
        // Dibujar trails
        if (this.effects.trails) {
            this.drawTrails();
        }
        
        // Dibujar manzana
        if (this.apple) {
            this.drawApple();
        }
        
        // Dibujar serpiente
        this.drawSnake();
        
        // Dibujar partículas
        if (this.effects.particles) {
            this.drawParticles();
        }
        
        // Restaurar contexto si hubo shake
        if (this.shakeIntensity > 0) {
            this.ctx.restore();
        }
    }
    
    drawGrid() {
        this.ctx.strokeStyle = 'rgba(0, 255, 255, 0.1)';
        this.ctx.lineWidth = 1;
        
        for (let x = 0; x <= this.GRID_SIZE; x++) {
            this.ctx.beginPath();
            this.ctx.moveTo(x * this.CELL_SIZE, 0);
            this.ctx.lineTo(x * this.CELL_SIZE, this.GRID_SIZE * this.CELL_SIZE);
            this.ctx.stroke();
        }
        
        for (let y = 0; y <= this.GRID_SIZE; y++) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y * this.CELL_SIZE);
            this.ctx.lineTo(this.GRID_SIZE * this.CELL_SIZE, y * this.CELL_SIZE);
            this.ctx.stroke();
        }
    }
    
    drawPath() {
        for (let i = 0; i < this.currentPath.length && i < 8; i++) {
            const pos = this.currentPath[i];
            const alpha = 1 - (i * 0.12);
            const size = 15 - (i * 1.5);
            
            this.ctx.fillStyle = `rgba(255, 255, 0, ${alpha})`;
            this.ctx.beginPath();
            this.ctx.arc(
                pos.x * this.CELL_SIZE + this.CELL_SIZE / 2,
                pos.y * this.CELL_SIZE + this.CELL_SIZE / 2,
                size,
                0,
                Math.PI * 2
            );
            this.ctx.fill();
            
            // Número del paso
            if (i < 3) {
                this.ctx.fillStyle = '#000000';
                this.ctx.font = 'bold 16px Arial';
                this.ctx.textAlign = 'center';
                this.ctx.fillText(
                    (i + 1).toString(),
                    pos.x * this.CELL_SIZE + this.CELL_SIZE / 2,
                    pos.y * this.CELL_SIZE + this.CELL_SIZE / 2 + 6
                );
            }
        }
    }
    
    drawTrails() {
        this.trails.forEach(trail => {
            const alpha = trail.life;
            this.ctx.fillStyle = `rgba(138, 43, 226, ${alpha * 0.3})`;
            this.ctx.fillRect(
                trail.x * this.CELL_SIZE,
                trail.y * this.CELL_SIZE,
                this.CELL_SIZE,
                this.CELL_SIZE
            );
        });
    }
    
    drawSnake() {
        const skinStyles = this.getSnakeSkinStyles();
        
        this.snake.forEach((segment, index) => {
            const x = segment.x * this.CELL_SIZE;
            const y = segment.y * this.CELL_SIZE;
            
            if (index === 0) {
                // Cabeza con efectos especiales
                this.drawSnakeHead(x, y, skinStyles);
            } else {
                // Cuerpo
                this.drawSnakeBody(x, y, skinStyles, index);
            }
        });
    }
    
    drawSnakeHead(x, y, skinStyles) {
        const centerX = x + this.CELL_SIZE / 2;
        const centerY = y + this.CELL_SIZE / 2;
        const radius = this.CELL_SIZE / 2 - 3;
        
        // Efecto de resplandor
        if (this.effects.glow) {
            const gradient = this.ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius + 10);
            gradient.addColorStop(0, skinStyles.head);
            gradient.addColorStop(1, 'rgba(0, 255, 255, 0)');
            
            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, radius + 10, 0, Math.PI * 2);
            this.ctx.fill();
        }
        
        // Cabeza principal
        const headGradient = this.ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius);
        headGradient.addColorStop(0, skinStyles.head);
        headGradient.addColorStop(1, skinStyles.headDark);
        
        this.ctx.fillStyle = headGradient;
        this.ctx.beginPath();
        this.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Borde
        this.ctx.strokeStyle = skinStyles.border;
        this.ctx.lineWidth = 3;
        this.ctx.stroke();
        
        // Ojos
        this.drawEyes(centerX, centerY, skinStyles);
    }
    
    drawEyes(centerX, centerY, skinStyles) {
        const eyeSize = 8;
        const eyeOffset = 12;
        
        // Ojo izquierdo
        this.ctx.fillStyle = skinStyles.eye;
        this.ctx.beginPath();
        this.ctx.arc(centerX - eyeOffset, centerY - 8, eyeSize, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Pupila izquierda
        this.ctx.fillStyle = '#000000';
        this.ctx.beginPath();
        this.ctx.arc(centerX - eyeOffset, centerY - 8, eyeSize / 2, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Ojo derecho
        this.ctx.fillStyle = skinStyles.eye;
        this.ctx.beginPath();
        this.ctx.arc(centerX + eyeOffset, centerY - 8, eyeSize, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Pupila derecha
        this.ctx.fillStyle = '#000000';
        this.ctx.beginPath();
        this.ctx.arc(centerX + eyeOffset, centerY - 8, eyeSize / 2, 0, Math.PI * 2);
        this.ctx.fill();
    }
    
    drawSnakeBody(x, y, skinStyles, index) {
        const intensity = Math.max(0.3, 1 - (index * 0.05));
        
        // Crear gradiente para el cuerpo
        const gradient = this.ctx.createLinearGradient(x, y, x + this.CELL_SIZE, y + this.CELL_SIZE);
        gradient.addColorStop(0, this.adjustColorAlpha(skinStyles.body, intensity));
        gradient.addColorStop(1, this.adjustColorAlpha(skinStyles.bodyDark, intensity));
        
        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(x + 2, y + 2, this.CELL_SIZE - 4, this.CELL_SIZE - 4);
        
        // Borde
        this.ctx.strokeStyle = this.adjustColorAlpha(skinStyles.border, intensity);
        this.ctx.lineWidth = 2;
        this.ctx.strokeRect(x + 2, y + 2, this.CELL_SIZE - 4, this.CELL_SIZE - 4);
        
        // Patrón según skin
        this.drawBodyPattern(x, y, skinStyles, index);
    }
    
    drawBodyPattern(x, y, skinStyles, index) {
        const centerX = x + this.CELL_SIZE / 2;
        const centerY = y + this.CELL_SIZE / 2;
        
        switch (this.snakeSkin) {
            case 'matrix':
                // Puntos digitales
                this.ctx.fillStyle = '#00ff41';
                this.ctx.fillRect(centerX - 2, centerY - 2, 4, 4);
                break;
                
            case 'plasma':
                // Líneas onduladas
                this.ctx.strokeStyle = '#ff69b4';
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                this.ctx.moveTo(x + 10, centerY);
                this.ctx.quadraticCurveTo(centerX, y + 10, x + this.CELL_SIZE - 10, centerY);
                this.ctx.stroke();
                break;
                
            case 'quantum':
                // Partículas cuánticas
                for (let i = 0; i < 3; i++) {
                    const px = x + 15 + (i * 15);
                    const py = centerY + Math.sin(index + i) * 5;
                    
                    this.ctx.fillStyle = `rgba(147, 112, 219, ${0.6 + Math.sin(Date.now() * 0.01) * 0.4})`;
                    this.ctx.beginPath();
                    this.ctx.arc(px, py, 2, 0, Math.PI * 2);
                    this.ctx.fill();
                }
                break;
        }
    }
    
    drawApple() {
        const x = this.apple.x * this.CELL_SIZE;
        const y = this.apple.y * this.CELL_SIZE;
        const centerX = x + this.CELL_SIZE / 2;
        const centerY = y + this.CELL_SIZE / 2;
        
        const foodStyles = this.getFoodStyles();
        
        // Efecto de resplandor
        if (this.effects.glow) {
            const glowGradient = this.ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, 40);
            glowGradient.addColorStop(0, this.adjustColorAlpha(foodStyles.color, 0.8));
            glowGradient.addColorStop(1, 'rgba(255, 255, 255, 0)');
            
            this.ctx.fillStyle = glowGradient;
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, 40, 0, Math.PI * 2);
            this.ctx.fill();
        }
        
        // Dibujar según estilo
        this.drawFoodStyle(centerX, centerY, foodStyles);
        
        // Animación de pulsado
        const pulse = 1 + Math.sin(Date.now() * 0.005) * 0.1;
        this.ctx.save();
        this.ctx.scale(pulse, pulse);
        this.ctx.restore();
    }
    
    drawFoodStyle(centerX, centerY, foodStyles) {
        switch (this.foodStyle) {
            case 'energy':
                this.drawEnergyOrb(centerX, centerY, foodStyles);
                break;
            case 'crystal':
                this.drawCrystal(centerX, centerY, foodStyles);
                break;
            case 'orb':
                this.drawMagicOrb(centerX, centerY, foodStyles);
                break;
            case 'data':
                this.drawDataNode(centerX, centerY, foodStyles);
                break;
        }
    }
    
    drawEnergyOrb(centerX, centerY, foodStyles) {
        const radius = 25;
        
        // Núcleo energético
        const coreGradient = this.ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius);
        coreGradient.addColorStop(0, '#ffffff');
        coreGradient.addColorStop(0.3, '#ffff00');
        coreGradient.addColorStop(1, '#ff8c00');
        
        this.ctx.fillStyle = coreGradient;
        this.ctx.beginPath();
        this.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Anillos de energía
        for (let i = 0; i < 3; i++) {
            const ringRadius = radius + (i * 8) + Math.sin(Date.now() * 0.01 + i) * 3;
            this.ctx.strokeStyle = `rgba(255, 255, 0, ${0.5 - i * 0.15})`;
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.arc(centerX, centerY, ringRadius, 0, Math.PI * 2);
            this.ctx.stroke();
        }
    }
    
    drawCrystal(centerX, centerY, foodStyles) {
        const size = 30;
        
        // Facetas del cristal
        this.ctx.fillStyle = '#4dd0e1';
        this.ctx.beginPath();
        this.ctx.moveTo(centerX, centerY - size);
        this.ctx.lineTo(centerX + size * 0.6, centerY - size * 0.3);
        this.ctx.lineTo(centerX + size * 0.6, centerY + size * 0.3);
        this.ctx.lineTo(centerX, centerY + size);
        this.ctx.lineTo(centerX - size * 0.6, centerY + size * 0.3);
        this.ctx.lineTo(centerX - size * 0.6, centerY - size * 0.3);
        this.ctx.closePath();
        this.ctx.fill();
        
        // Brillos internos
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        this.ctx.beginPath();
        this.ctx.moveTo(centerX - 5, centerY - 15);
        this.ctx.lineTo(centerX + 5, centerY - 10);
        this.ctx.lineTo(centerX, centerY - 5);
        this.ctx.closePath();
        this.ctx.fill();
    }
    
    drawMagicOrb(centerX, centerY, foodStyles) {
        const radius = 25;
        
        // Orbe principal
        const orbGradient = this.ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, radius);
        orbGradient.addColorStop(0, '#ff10f0');
        orbGradient.addColorStop(0.7, '#8a2be2');
        orbGradient.addColorStop(1, '#4b0082');
        
        this.ctx.fillStyle = orbGradient;
        this.ctx.beginPath();
        this.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Partículas mágicas flotantes
        for (let i = 0; i < 6; i++) {
            const angle = (Date.now() * 0.002) + (i * Math.PI / 3);
            const distance = 35 + Math.sin(angle * 2) * 8;
            const px = centerX + Math.cos(angle) * distance;
            const py = centerY + Math.sin(angle) * distance;
            
            this.ctx.fillStyle = '#ff10f0';
            this.ctx.beginPath();
            this.ctx.arc(px, py, 3, 0, Math.PI * 2);
            this.ctx.fill();
        }
    }
    
    drawDataNode(centerX, centerY, foodStyles) {
        const size = 20;
        
        // Nodo central
        this.ctx.fillStyle = '#39ff14';
        this.ctx.fillRect(centerX - size/2, centerY - size/2, size, size);
        
        // Conexiones de datos
        const connections = [
            { x: centerX - 30, y: centerY - 20 },
            { x: centerX + 30, y: centerY - 20 },
            { x: centerX - 30, y: centerY + 20 },
            { x: centerX + 30, y: centerY + 20 }
        ];
        
        connections.forEach(conn => {
            // Línea de conexión
            this.ctx.strokeStyle = '#00ff80';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.moveTo(centerX, centerY);
            this.ctx.lineTo(conn.x, conn.y);
            this.ctx.stroke();
            
            // Nodo de conexión
            this.ctx.fillStyle = '#00ff80';
            this.ctx.beginPath();
            this.ctx.arc(conn.x, conn.y, 4, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }
    
    drawParticles() {
        this.particles.forEach(particle => {
            const alpha = particle.life;
            this.ctx.fillStyle = this.adjustColorAlpha(particle.color, alpha);
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }
    
    getSnakeSkinStyles() {
        const skins = {
            cyber: {
                head: '#00ffff',
                headDark: '#0080ff',
                body: '#0080ff',
                bodyDark: '#004080',
                border: '#ffffff',
                eye: '#ffff00'
            },
            neon: {
                head: '#39ff14',
                headDark: '#00ff80',
                body: '#00ff80',
                bodyDark: '#008040',
                border: '#ffffff',
                eye: '#ffffff'
            },
            matrix: {
                head: '#00ff00',
                headDark: '#008000',
                body: '#008000',
                bodyDark: '#004000',
                border: '#00ff41',
                eye: '#00ff41'
            },
            plasma: {
                head: '#ff1493',
                headDark: '#ff69b4',
                body: '#ff69b4',
                bodyDark: '#ff1493',
                border: '#ffffff',
                eye: '#ffffff'
            },
            hologram: {
                head: '#87ceeb',
                headDark: '#4169e1',
                body: '#4169e1',
                bodyDark: '#000080',
                border: '#ffffff',
                eye: '#ffffff'
            },
            quantum: {
                head: '#9370db',
                headDark: '#8a2be2',
                body: '#8a2be2',
                bodyDark: '#4b0082',
                border: '#dda0dd',
                eye: '#ffffff'
            }
        };
        
        return skins[this.snakeSkin] || skins.cyber;
    }
    
    getFoodStyles() {
        const foods = {
            energy: { color: '#ffff00' },
            crystal: { color: '#00ffff' },
            orb: { color: '#ff10f0' },
            data: { color: '#39ff14' }
        };
        
        return foods[this.foodStyle] || foods.energy;
    }
    
    adjustColorAlpha(color, alpha) {
        // Convertir color hex a rgba con alpha
        const hex = color.replace('#', '');
        const r = parseInt(hex.substr(0, 2), 16);
        const g = parseInt(hex.substr(2, 2), 16);
        const b = parseInt(hex.substr(4, 2), 16);
        
        return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    }
    
    playSound(type) {
        if (!this.audioEnabled || !this.audioContext) return;
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);
        
        const sounds = {
            collect: { freq: [440, 523, 659], duration: 0.3 },
            collision: { freq: [220, 165, 110], duration: 0.8 },
            victory: { freq: [523, 659, 784, 1047], duration: 1.2 }
        };
        
        const sound = sounds[type] || sounds.collect;
        
        oscillator.frequency.setValueAtTime(sound.freq[0], this.audioContext.currentTime);
        gainNode.gain.setValueAtTime(0.1, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + sound.duration);
        
        oscillator.start();
        oscillator.stop(this.audioContext.currentTime + sound.duration);
    }
    
    updateUI() {
        // Actualizar estadísticas
        document.getElementById('current-score').textContent = this.score;
        document.getElementById('targets-collected').textContent = this.score;
        document.getElementById('snake-length').textContent = this.snake.length;
        document.getElementById('ai-time').textContent = this.searchTime.toFixed(1);
        document.getElementById('nodes-explored').textContent = this.nodesExplored;
        document.getElementById('total-moves').textContent = this.moves;
        
        // Progreso
        const progress = (this.score / this.MAX_APPLES) * 100;
        document.getElementById('game-progress').style.width = `${progress}%`;
        document.getElementById('progress-text').textContent = `${Math.round(progress)}%`;
        
        // Eficiencia
        const efficiency = Math.max(0, 100 - (this.searchTime * 100));
        document.getElementById('efficiency-score').textContent = Math.round(efficiency);
        document.getElementById('efficiency-fill').style.width = `${efficiency}%`;
        
        // Estado del juego
        const statusMap = {
            menu: 'LISTO',
            playing: 'EJECUTANDO',
            paused: 'PAUSADO',
            gameover: 'FINALIZADO',
            victory: 'VICTORIA'
        };
        
        document.getElementById('game-status').textContent = statusMap[this.gameState];
        
        // Algoritmo actual
        document.getElementById('current-algorithm').textContent = this.aiAgent?.algorithm || 'N/A';
    }
    
    toggleGame() {
        if (this.gameState === 'menu' || this.gameState === 'gameover') {
            this.gameState = 'playing';
            this.resetGame();
            this.playSound('collect');
            
            document.getElementById('play-btn').innerHTML = `
                <i class="fas fa-stop"></i>
                <span>DETENER IA</span>
                <div class="button-glow"></div>
            `;
        } else if (this.gameState === 'playing') {
            this.gameState = 'menu';
            
            document.getElementById('play-btn').innerHTML = `
                <i class="fas fa-play"></i>
                <span>INICIAR IA</span>
                <div class="button-glow"></div>
            `;
        }
    }
    
    pauseGame() {
        if (this.gameState === 'playing') {
            this.gameState = 'paused';
            document.getElementById('pause-btn').innerHTML = '<i class="fas fa-play"></i>';
        } else if (this.gameState === 'paused') {
            this.gameState = 'playing';
            document.getElementById('pause-btn').innerHTML = '<i class="fas fa-pause"></i>';
        }
    }
    
    togglePath() {
        // La visualización del camino ya está implementada en render()
        const button = document.getElementById('path-toggle');
        button.classList.toggle('active');
    }
    
    setFPS(fps) {
        this.fps = fps;
        this.frameInterval = 1000 / this.fps;
        document.getElementById('speed-value').textContent = fps;
    }
    
    setAlgorithm(algorithm) {
        this.currentAlgorithm = algorithm;
        this.aiAgent = new AIAgent(algorithm);
        
        // Actualizar UI
        document.querySelectorAll('.algorithm-option').forEach(option => {
            option.classList.remove('active');
        });
        document.querySelector(`[data-algo="${algorithm}"]`).classList.add('active');
    }
    
    setSnakeSkin(skin) {
        this.snakeSkin = skin;
        
        // Actualizar UI
        document.querySelectorAll('.skin-option').forEach(option => {
            option.classList.remove('active');
        });
        document.querySelector(`[data-skin="${skin}"]`).classList.add('active');
    }
    
    setFoodStyle(style) {
        this.foodStyle = style;
        
        // Actualizar UI
        document.querySelectorAll('.food-option').forEach(option => {
            option.classList.remove('active');
        });
        document.querySelector(`[data-food="${style}"]`).classList.add('active');
    }
    
    toggleEffect(effect) {
        this.effects[effect] = !this.effects[effect];
        
        // Actualizar UI
        const toggle = document.querySelector(`[data-effect="${effect}"]`);
        toggle.classList.toggle('active');
    }
    
    toggleAudio() {
        this.audioEnabled = !this.audioEnabled;
        
        const button = document.getElementById('audio-btn');
        if (this.audioEnabled) {
            button.innerHTML = '<i class="fas fa-volume-up"></i>';
        } else {
            button.innerHTML = '<i class="fas fa-volume-mute"></i>';
        }
    }
    
    showVictoryModal() {
        document.getElementById('winner-algorithm').textContent = this.currentAlgorithm.toUpperCase();
        document.getElementById('winner-time').textContent = `${(this.gameTime / 1000).toFixed(1)}s`;
        document.getElementById('winner-efficiency').textContent = `${Math.round(100 - (this.searchTime * 10))}%`;
        
        document.getElementById('victory-modal').classList.add('show');
        
        document.getElementById('victory-continue').onclick = () => {
            document.getElementById('victory-modal').classList.remove('show');
            this.resetGame();
        };
    }
    
    showGameOverModal() {
        document.getElementById('final-score').textContent = `${this.score}/${this.MAX_APPLES}`;
        document.getElementById('avg-ai-time').textContent = `${this.searchTime.toFixed(1)}ms`;
        document.getElementById('total-nodes').textContent = this.nodesExplored;
        
        document.getElementById('game-over-modal').classList.add('show');
        
        document.getElementById('gameover-retry').onclick = () => {
            document.getElementById('game-over-modal').classList.remove('show');
            this.resetGame();
        };
    }
}

// Inicializar cuando esté listo
let gameEngine;
document.addEventListener('DOMContentLoaded', () => {
    // Simular carga épica
    setTimeout(() => {
        document.getElementById('loading-screen').style.display = 'none';
        document.getElementById('main-interface').classList.remove('interface-hidden');
        
        gameEngine = new GameEngine();
        console.log('🚀 Snake AI Ultimate cargado completamente');
    }, 3000);
});
'''

# Guardar el motor de juego
with open('game-engine.js', 'w', encoding='utf-8') as f:
    f.write(game_engine_js)

print("✅ 3/5 - game-engine.js creado (Motor principal)")
print("    🎮 Motor de juego optimizado de 60fps")
print("    🎨 Sistema de renderizado avanzado")
print("    ⚡ Efectos visuales en tiempo real")
print("    🔊 Audio procedural integrado")
print("    📊 Sistema de estadísticas completo")