// 🧠 AI ALGORITHMS - INTELIGENCIA ARTIFICIAL AVANZADA
// Implementación profesional de algoritmos de búsqueda para Snake AI

class AIAgent {
    constructor(algorithm = 'astar') {
        this.algorithm = algorithm;
        this.lastSearchTime = 0;
        this.lastNodesExplored = 0;
        this.searchHistory = [];
        this.totalSearches = 0;
        this.totalSearchTime = 0;
        this.performanceStats = {
            astar: { avgTime: 0, avgNodes: 0, efficiency: 95 },
            bfs: { avgTime: 0, avgNodes: 0, efficiency: 87 },
            dfs: { avgTime: 0, avgNodes: 0, efficiency: 78 },
            dijkstra: { avgTime: 0, avgNodes: 0, efficiency: 82 }
        };

        console.log(`🧠 AI Agent inicializado con algoritmo: ${algorithm.toUpperCase()}`);
    }

    getNextMove(snake, apple, gridSize) {
        if (!apple || snake.length === 0) {
            return this.getSurvivalMove(snake, gridSize);
        }

        const startTime = performance.now();
        const head = snake[0];
        const target = apple;

        // Crear mapa de obstáculos (cuerpo de la serpiente excepto la cola)
        const obstacles = new Set();
        for (let i = 1; i < snake.length - 1; i++) {
            obstacles.add(`${snake[i].x},${snake[i].y}`);
        }

        // Encontrar camino según algoritmo
        let path = [];
        let nodesExplored = 0;

        switch (this.algorithm) {
            case 'astar':
                { const result = this.aStar(head, target, obstacles, gridSize);
                  path = result.path; nodesExplored = result.nodesExplored; }
                break;
            case 'bfs':
                { const result = this.bfs(head, target, obstacles, gridSize);
                  path = result.path; nodesExplored = result.nodesExplored; }
                break;
            case 'dfs':
                { const result = this.dfs(head, target, obstacles, gridSize);
                  path = result.path; nodesExplored = result.nodesExplored; }
                break;
            case 'dijkstra':
                { const result = this.dijkstra(head, target, obstacles, gridSize);
                  path = result.path; nodesExplored = result.nodesExplored; }
                break;
        }

        // Registrar métricas
        const searchTime = performance.now() - startTime;
        this.recordSearch(searchTime, nodesExplored);

        // Determinar dirección del movimiento
        if (path.length > 1) {
            const nextPos = path[1];
            const dx = nextPos.x - head.x;
            const dy = nextPos.y - head.y;

            if (dx === 1) return 'right';
            if (dx === -1) return 'left';
            if (dy === 1) return 'down';
            if (dy === -1) return 'up';
        }

        // Estrategia de supervivencia si no hay camino
        return this.getSurvivalMove(snake, gridSize);
    }

    // A* - Algoritmo heurístico optimizado
    aStar(start, goal, obstacles, gridSize) {
        const openSet = new MinHeap();
        const closedSet = new Set();
        const gScore = new Map();
        const fScore = new Map();
        const parent = new Map();

        const startKey = `${start.x},${start.y}`;
        const goalKey = `${goal.x},${goal.y}`;

        gScore.set(startKey, 0);
        fScore.set(startKey, this.manhattanDistance(start, goal));
        openSet.insert({ pos: start, key: startKey, f: fScore.get(startKey) });

        let nodesExplored = 0;

        while (!openSet.isEmpty()) {
            const current = openSet.extractMin();
            const currentKey = current.key;

            if (closedSet.has(currentKey)) continue;
            closedSet.add(currentKey);
            nodesExplored++;

            // Encontrado el objetivo
            if (currentKey === goalKey) {
                return {
                    path: this.reconstructPath(parent, currentKey, start),
                    nodesExplored
                };
            }

            // Explorar vecinos
            const neighbors = this.getNeighbors(current.pos, gridSize);
            for (const neighbor of neighbors) {
                const neighborKey = `${neighbor.x},${neighbor.y}`;

                if (closedSet.has(neighborKey) || obstacles.has(neighborKey)) {
                    continue;
                }

                const tentativeG = gScore.get(currentKey) + 1;

                if (!gScore.has(neighborKey) || tentativeG < gScore.get(neighborKey)) {
                    parent.set(neighborKey, current.pos);
                    gScore.set(neighborKey, tentativeG);

                    const h = this.manhattanDistance(neighbor, goal);
                    const f = tentativeG + h;
                    fScore.set(neighborKey, f);

                    openSet.insert({ pos: neighbor, key: neighborKey, f });
                }
            }
        }

        return { path: [], nodesExplored };
    }

    // BFS - Breadth-First Search garantizado
    bfs(start, goal, obstacles, gridSize) {
        const queue = [{ pos: start, path: [start] }];
        const visited = new Set([`${start.x},${start.y}`]);
        const goalKey = `${goal.x},${goal.y}`;

        let nodesExplored = 0;

        while (queue.length > 0) {
            const { pos: current, path } = queue.shift();
            const currentKey = `${current.x},${current.y}`;
            nodesExplored++;

            // Encontrado el objetivo
            if (currentKey === goalKey) {
                return { path, nodesExplored };
            }

            // Explorar vecinos
            const neighbors = this.getNeighbors(current, gridSize);
            for (const neighbor of neighbors) {
                const neighborKey = `${neighbor.x},${neighbor.y}`;

                if (!visited.has(neighborKey) && !obstacles.has(neighborKey)) {
                    visited.add(neighborKey);
                    queue.push({
                        pos: neighbor,
                        path: [...path, neighbor]
                    });
                }
            }
        }

        return { path: [], nodesExplored };
    }

    // DFS - Depth-First Search eficiente en memoria
    dfs(start, goal, obstacles, gridSize) {
        const stack = [{ pos: start, path: [start] }];
        const visited = new Set();
        const goalKey = `${goal.x},${goal.y}`;

        let nodesExplored = 0;

        while (stack.length > 0) {
            const { pos: current, path } = stack.pop();
            const currentKey = `${current.x},${current.y}`;

            if (visited.has(currentKey)) continue;
            visited.add(currentKey);
            nodesExplored++;

            // Encontrado el objetivo
            if (currentKey === goalKey) {
                return { path, nodesExplored };
            }

            // Explorar vecinos (en orden aleatorio para variabilidad)
            const neighbors = this.getNeighbors(current, gridSize);
            this.shuffleArray(neighbors);

            for (const neighbor of neighbors) {
                const neighborKey = `${neighbor.x},${neighbor.y}`;

                if (!visited.has(neighborKey) && !obstacles.has(neighborKey)) {
                    stack.push({
                        pos: neighbor,
                        path: [...path, neighbor]
                    });
                }
            }
        }

        return { path: [], nodesExplored };
    }

    // Dijkstra - Uniform Cost Search
    dijkstra(start, goal, obstacles, gridSize) {
        const distances = new Map();
        const previous = new Map();
        const unvisited = new MinHeap();
        const visited = new Set();

        const startKey = `${start.x},${start.y}`;
        const goalKey = `${goal.x},${goal.y}`;

        // Inicializar distancias
        for (let x = 0; x < gridSize; x++) {
            for (let y = 0; y < gridSize; y++) {
                const key = `${x},${y}`;
                distances.set(key, Infinity);
            }
        }

        distances.set(startKey, 0);
        unvisited.insert({ pos: start, key: startKey, distance: 0 });

        let nodesExplored = 0;

        while (!unvisited.isEmpty()) {
            const current = unvisited.extractMin();
            const currentKey = current.key;

            if (visited.has(currentKey)) continue;
            visited.add(currentKey);
            nodesExplored++;

            // Encontrado el objetivo
            if (currentKey === goalKey) {
                return {
                    path: this.reconstructDijkstraPath(previous, goalKey, start),
                    nodesExplored
                };
            }

            // Si la distancia actual es infinita, no hay camino
            if (distances.get(currentKey) === Infinity) break;

            // Explorar vecinos
            const neighbors = this.getNeighbors(current.pos, gridSize);
            for (const neighbor of neighbors) {
                const neighborKey = `${neighbor.x},${neighbor.y}`;

                if (visited.has(neighborKey) || obstacles.has(neighborKey)) {
                    continue;
                }

                const altDistance = distances.get(currentKey) + 1;

                if (altDistance < distances.get(neighborKey)) {
                    distances.set(neighborKey, altDistance);
                    previous.set(neighborKey, current.pos);

                    unvisited.insert({
                        pos: neighbor,
                        key: neighborKey,
                        distance: altDistance
                    });
                }
            }
        }

        return { path: [], nodesExplored };
    }

    // Obtener camino para visualización
    getPath(snake, apple, gridSize) {
        if (!apple || snake.length === 0) return [];

        const head = snake[0];
        const obstacles = new Set();

        // Crear obstáculos (cuerpo sin cola)
        for (let i = 1; i < snake.length - 1; i++) {
            obstacles.add(`${snake[i].x},${snake[i].y}`);
        }

        // Obtener camino según algoritmo actual
        let result = { path: [], nodesExplored: 0 };

        switch (this.algorithm) {
            case 'astar':
                result = this.aStar(head, apple, obstacles, gridSize);
                break;
            case 'bfs':
                result = this.bfs(head, apple, obstacles, gridSize);
                break;
            case 'dfs':
                result = this.dfs(head, apple, obstacles, gridSize);
                break;
            case 'dijkstra':
                result = this.dijkstra(head, apple, obstacles, gridSize);
                break;
        }

        // Retornar solo los primeros 8 pasos para visualización
        return result.path.slice(1, 9);
    }

    // Estrategia de supervivencia cuando no hay camino directo
    getSurvivalMove(snake, gridSize) {
        if (snake.length === 0) return 'right';

        const head = snake[0];
        const directions = ['up', 'down', 'left', 'right'];
        const safeDirections = [];

        // Evaluar cada dirección
        for (const direction of directions) {
            const newPos = this.getPositionInDirection(head, direction);

            if (this.isValidPosition(newPos, gridSize) && 
                !this.isCollisionWithSelf(newPos, snake)) {

                // Calcular puntuación de supervivencia
                const score = this.calculateSurvivalScore(newPos, snake, gridSize);
                safeDirections.push({ direction, score });
            }
        }

        if (safeDirections.length === 0) {
            // Situación desesperada - elegir cualquier dirección válida
            for (const direction of directions) {
                const newPos = this.getPositionInDirection(head, direction);
                if (this.isValidPosition(newPos, gridSize)) {
                    return direction;
                }
            }
            return 'right'; // Fallback
        }

        // Elegir la dirección con mejor puntuación
        safeDirections.sort((a, b) => b.score - a.score);
        return safeDirections[0].direction;
    }

    // Calcular puntuación de supervivencia para una posición
    calculateSurvivalScore(pos, snake, gridSize) {
        let score = 0;

        // Distancia a las paredes (preferir centro)
        const wallDistance = Math.min(
            pos.x, 
            pos.y, 
            gridSize - 1 - pos.x, 
            gridSize - 1 - pos.y
        );
        score += wallDistance * 10;

        // Espacio libre alrededor
        const neighbors = this.getNeighbors(pos, gridSize);
        const freeNeighbors = neighbors.filter(n => 
            !this.isCollisionWithSelf(n, snake)
        ).length;
        score += freeNeighbors * 25;

        // Evitar estar cerca de la cola
        if (snake.length > 3) {
            const tail = snake[snake.length - 1];
            const tailDistance = this.manhattanDistance(pos, tail);
            score += Math.min(tailDistance, 5) * 5;
        }

        return score;
    }

    // Utilidades de pathfinding
    getNeighbors(pos, gridSize) {
        const neighbors = [];
        const directions = [
            { x: 0, y: -1 }, // up
            { x: 0, y: 1 },  // down
            { x: -1, y: 0 }, // left
            { x: 1, y: 0 }   // right
        ];

        for (const dir of directions) {
            const newPos = { x: pos.x + dir.x, y: pos.y + dir.y };
            if (this.isValidPosition(newPos, gridSize)) {
                neighbors.push(newPos);
            }
        }

        return neighbors;
    }

    isValidPosition(pos, gridSize) {
        return pos.x >= 0 && pos.x < gridSize && pos.y >= 0 && pos.y < gridSize;
    }

    isCollisionWithSelf(pos, snake) {
        return snake.some(segment => segment.x === pos.x && segment.y === pos.y);
    }

    getPositionInDirection(pos, direction) {
        const directions = {
            'up': { x: pos.x, y: pos.y - 1 },
            'down': { x: pos.x, y: pos.y + 1 },
            'left': { x: pos.x - 1, y: pos.y },
            'right': { x: pos.x + 1, y: pos.y }
        };

        return directions[direction] || pos;
    }

    manhattanDistance(a, b) {
        return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    }

    // Reconstruir camino desde los nodos padre
    reconstructPath(parent, goalKey, start) {
        const path = [];
        let currentKey = goalKey;

        while (currentKey) {
            const [x, y] = currentKey.split(',').map(Number);
            path.unshift({ x, y });

            const parentPos = parent.get(currentKey);
            if (!parentPos) break;

            currentKey = `${parentPos.x},${parentPos.y}`;

            // Evitar bucle infinito
            if (parentPos.x === start.x && parentPos.y === start.y) {
                path.unshift(start);
                break;
            }
        }

        return path;
    }

    reconstructDijkstraPath(previous, goalKey, start) {
        const path = [];
        let currentKey = goalKey;

        while (currentKey) {
            const [x, y] = currentKey.split(',').map(Number);
            path.unshift({ x, y });

            const prev = previous.get(currentKey);
            if (!prev) break;

            currentKey = `${prev.x},${prev.y}`;

            if (prev.x === start.x && prev.y === start.y) {
                path.unshift(start);
                break;
            }
        }

        return path;
    }

    // Utilidad para mezclar array (Fisher-Yates)
    shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    // Registrar búsqueda para estadísticas
    recordSearch(searchTime, nodesExplored) {
        this.lastSearchTime = searchTime;
        this.lastNodesExplored = nodesExplored;
        this.totalSearches++;
        this.totalSearchTime += searchTime;

        // Actualizar estadísticas del algoritmo
        const stats = this.performanceStats[this.algorithm];
        if (stats) {
            stats.avgTime = this.totalSearchTime / this.totalSearches;
            stats.avgNodes = (stats.avgNodes * (this.totalSearches - 1) + nodesExplored) / this.totalSearches;

            // Calcular eficiencia basada en tiempo y nodos
            const timeEfficiency = Math.max(0, 100 - (stats.avgTime * 100));
            const nodeEfficiency = Math.max(0, 100 - (stats.avgNodes - 10));
            stats.efficiency = (timeEfficiency + nodeEfficiency) / 2;
        }

        // Mantener historial limitado
        this.searchHistory.push({ time: searchTime, nodes: nodesExplored, algorithm: this.algorithm });
        if (this.searchHistory.length > 100) {
            this.searchHistory.shift();
        }
    }

    // Obtener estadísticas de rendimiento
    getPerformanceStats() {
        return {
            currentAlgorithm: this.algorithm,
            lastSearchTime: this.lastSearchTime,
            lastNodesExplored: this.lastNodesExplored,
            totalSearches: this.totalSearches,
            averageTime: this.totalSearchTime / Math.max(1, this.totalSearches),
            algorithmStats: this.performanceStats,
            searchHistory: this.searchHistory.slice(-20) // Últimas 20 búsquedas
        };
    }

    // Cambiar algoritmo
    setAlgorithm(algorithm) {
        if (['astar', 'bfs', 'dfs', 'dijkstra'].includes(algorithm)) {
            this.algorithm = algorithm;
            console.log(`🔄 Algoritmo cambiado a: ${algorithm.toUpperCase()}`);
            return true;
        }
        return false;
    }
}

// MinHeap para algoritmos que requieren cola de prioridad
class MinHeap {
    constructor() {
        this.heap = [];
    }

    parent(i) { return Math.floor((i - 1) / 2); }
    leftChild(i) { return 2 * i + 1; }
    rightChild(i) { return 2 * i + 2; }

    swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    insert(item) {
        this.heap.push(item);
        this.heapifyUp(this.heap.length - 1);
    }

    heapifyUp(i) {
        const p = this.parent(i);
        if (p >= 0 && this.compare(this.heap[i], this.heap[p]) < 0) {
            this.swap(i, p);
            this.heapifyUp(p);
        }
    }

    extractMin() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown(0);
        return min;
    }

    heapifyDown(i) {
        const left = this.leftChild(i);
        const right = this.rightChild(i);
        let smallest = i;

        if (left < this.heap.length && this.compare(this.heap[left], this.heap[smallest]) < 0) {
            smallest = left;
        }

        if (right < this.heap.length && this.compare(this.heap[right], this.heap[smallest]) < 0) {
            smallest = right;
        }

        if (smallest !== i) {
            this.swap(i, smallest);
            this.heapifyDown(smallest);
        }
    }

    compare(a, b) {
        // Para A*, comparar por f score
        if (a.f !== undefined && b.f !== undefined) {
            return a.f - b.f;
        }
        // Para Dijkstra, comparar por distancia
        if (a.distance !== undefined && b.distance !== undefined) {
            return a.distance - b.distance;
        }
        return 0;
    }

    isEmpty() {
        return this.heap.length === 0;
    }

    size() {
        return this.heap.length;
    }
}

// Análisis comparativo de algoritmos
class AlgorithmAnalyzer {
    constructor() {
        this.results = [];
        this.benchmarkData = {
            astar: { avgTime: 0.8, avgNodes: 12, efficiency: 95 },
            bfs: { avgTime: 2.1, avgNodes: 18, efficiency: 87 },
            dfs: { avgTime: 1.5, avgNodes: 25, efficiency: 78 },
            dijkstra: { avgTime: 2.8, avgNodes: 22, efficiency: 82 }
        };
    }

    analyzePerformance(agent) {
        const stats = agent.getPerformanceStats();

        return {
            algorithm: stats.currentAlgorithm,
            efficiency: this.calculateEfficiency(stats),
            recommendation: this.getRecommendation(stats),
            comparison: this.compareWithBenchmark(stats)
        };
    }

    calculateEfficiency(stats) {
        const timeScore = Math.max(0, 100 - (stats.averageTime * 50));
        const nodeScore = Math.max(0, 100 - ((stats.lastNodesExplored - 8) * 5));
        return Math.round((timeScore + nodeScore) / 2);
    }

    getRecommendation(stats) {
        const algo = stats.currentAlgorithm;
        const recommendations = {
            astar: "Excelente balance velocidad-calidad. Ideal para uso general.",
            bfs: "Garantiza solución óptima. Perfecto para análisis académico.",
            dfs: "Eficiente en memoria. Recomendado para espacios grandes.",
            dijkstra: "Consistente y confiable. Ideal para comparaciones."
        };

        return recommendations[algo] || "Algoritmo en evaluación.";
    }

    compareWithBenchmark(stats) {
        const benchmark = this.benchmarkData[stats.currentAlgorithm];
        if (!benchmark) return null;

        return {
            timeComparison: stats.averageTime < benchmark.avgTime ? 'mejor' : 'esperado',
            nodeComparison: stats.lastNodesExplored < benchmark.avgNodes ? 'mejor' : 'esperado',
            overallRating: this.calculateRating(stats, benchmark)
        };
    }

    calculateRating(stats, benchmark) {
        const timeRatio = stats.averageTime / benchmark.avgTime;
        const nodeRatio = stats.lastNodesExplored / benchmark.avgNodes;
        const avgRatio = (timeRatio + nodeRatio) / 2;

        if (avgRatio < 0.8) return 'excelente';
        if (avgRatio < 1.2) return 'bueno';
        return 'aceptable';
    }
}

console.log('🧠 AI Algorithms module cargado correctamente');
console.log('   ⚡ A* Heuristic Search implementado');
console.log('   🔍 Breadth-First Search implementado'); 
console.log('   🌊 Depth-First Search implementado');
console.log('   📈 Dijkstra Uniform Cost implementado');
console.log('   📊 Sistema de análisis y métricas activo');
