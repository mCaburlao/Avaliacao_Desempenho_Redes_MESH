#!/bin/bash
# =============================================================================
# run_all_experiments.sh — Roda TODOS os experimentos AODV vs OLSR
#
# Topologias:
#   1. chain-9   (cadeia linear  9 nos)  duration=400s
#   2. grid-25   (grid 5x5      25 nos)  duration=500s
#   3. random-50 (aleatorio     50 nos)  duration=600s
#
# Uso:
#   ./run_all_experiments.sh             # roda tudo
#   ./run_all_experiments.sh --dry-run   # apenas mostra os comandos
#   ./run_all_experiments.sh chain-9     # roda so a topologia indicada
#   ./run_all_experiments.sh grid-25 random-50  # roda subset
# =============================================================================

set -euo pipefail

BASE=/mnt/d/OneDrive/Documentos/UFABC/2026.1/Avaliacao_Desempenho_Redes_MESH
MESHSIM=$BASE/MeshSim/build/sim/mesh_sim
NS3_LIB=$BASE/ns-3-dev/build/lib
EXPS=$BASE/experiments

# --- Parsear argumentos ---
DRY_RUN=0
RUN_TOPOLOGIES=()

for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=1 ;;
        grid-25|random-50|random-75|random-100|random-150|random-200|random-300|random-500|random-750|random-1000) RUN_TOPOLOGIES+=("$arg") ;;
        *) echo "Argumento desconhecido: $arg"; exit 1 ;;
    esac
done

# Sem argumento de topologia = roda tudo
if [ ${#RUN_TOPOLOGIES[@]} -eq 0 ]; then
    RUN_TOPOLOGIES=("grid-25" "random-50" "random-75" "random-100" "random-150" "random-200" "random-300" "random-500" "random-750" "random-1000")
fi

# --- Validacoes ---
if [ ! -f "$MESHSIM" ]; then
    echo "ERRO: mesh_sim nao encontrado: $MESHSIM"
    echo "  Compile: cd $BASE/MeshSim/build && make -j\$(nproc)"
    exit 1
fi

export LD_LIBRARY_PATH=$NS3_LIB:${LD_LIBRARY_PATH:-}


# =============================================================================
# Funcao auxiliar: rodar uma simulacao
# =============================================================================
run_sim() {
    local LABEL=$1
    local CONFIG=$2
    local OUT=$3
    local MESH_SIZE=$4
    local STA_SIZE=$5
    local DURATION=$6

    echo ""
    echo "┌─ [$(date +%H:%M:%S)] $LABEL"
    echo "│  config:   $(basename $CONFIG)"
    echo "│  saida:    $(realpath --relative-to=$BASE $OUT)"
    echo "│  params:   meshSize=$MESH_SIZE  staSize=$STA_SIZE  duration=${DURATION}s"

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "│  [DRY RUN] $MESHSIM --meshSize=$MESH_SIZE --staSize=$STA_SIZE"
        echo "│             --simDuration=$DURATION $CONFIG $OUT"
        echo "└─ (pulado)"
        return 0
    fi

    if [ ! -d "$CONFIG" ]; then
        echo "└─ ERRO: config nao encontrada: $CONFIG"
        echo "   Execute: python3 $EXPS/generate_all_configs.py"
        return 1
    fi

    mkdir -p "$OUT"
    # Limpar resultados anteriores para evitar mistura de runs
    rm -f "$OUT"/*.xml "$OUT"/*.txt "$OUT"/*.pcap 2>/dev/null || true

    START=$(date +%s)
    "$MESHSIM" \
        --meshSize=$MESH_SIZE \
        --staSize=$STA_SIZE \
        --simDuration=$DURATION \
        "$CONFIG" \
        "$OUT"
    END=$(date +%s)

    ELAPSED=$((END - START))
    echo "└─ concluido em ${ELAPSED}s"
}


# =============================================================================
# Funcao auxiliar: rodar AODV e OLSR da mesma topologia em PARALELO
#
# Args:  LABEL_A CONFIG_A OUT_A  LABEL_O CONFIG_O OUT_O  MESH_SZ STA_SZ DUR
#
# Executa os dois processos em background e aguarda ambos terminarem.
# Sai com erro se qualquer um dos dois falhar.
# =============================================================================
run_pair() {
    run_sim "$1" "$2" "$3" "$7" "$8" "$9" &
    local pid_a=$!
    run_sim "$4" "$5" "$6" "$7" "$8" "$9" &
    local pid_o=$!
    wait "$pid_a" || { echo "└─ ERRO: $1 falhou (pid $pid_a)"; exit 1; }
    wait "$pid_o" || { echo "└─ ERRO: $4 falhou (pid $pid_o)"; exit 1; }
}


# =============================================================================
# Funcao: gerar configs se necessario
# =============================================================================
ensure_configs() {
    local NEED_GEN=0
    for topo in "${RUN_TOPOLOGIES[@]}"; do
        case "$topo" in
            grid-25)    [ -d "$EXPS/grid_25nodes/config_AODV_seed100" ]    || NEED_GEN=1 ;;
            random-50)  [ -d "$EXPS/random_50nodes/config_AODV_seed200" ]  || NEED_GEN=1 ;;
            random-75)  [ -d "$EXPS/random_75nodes/config_AODV_seed210" ]  || NEED_GEN=1 ;;
            random-100) [ -d "$EXPS/random_100nodes/config_AODV_seed300" ] || NEED_GEN=1 ;;
            random-150) [ -d "$EXPS/random_150nodes/config_AODV_seed310" ] || NEED_GEN=1 ;;
            random-200) [ -d "$EXPS/random_200nodes/config_AODV_seed400" ] || NEED_GEN=1 ;;
            random-300) [ -d "$EXPS/random_300nodes/config_AODV_seed410" ] || NEED_GEN=1 ;;
            random-500) [ -d "$EXPS/random_500nodes/config_AODV_seed500" ] || NEED_GEN=1 ;;
            random-750) [ -d "$EXPS/random_750nodes/config_AODV_seed510" ] || NEED_GEN=1 ;;
            random-1000)[ -d "$EXPS/random_1000nodes/config_AODV_seed600" ]|| NEED_GEN=1 ;;
        esac
    done

    if [[ $NEED_GEN -eq 1 ]]; then
        echo ""
        echo ">>> Gerando configs ausentes..."
        python3 "$EXPS/generate_all_configs.py"
    fi
}


# =============================================================================
# Funcao: salvar resultados parciais apos cada topologia
# =============================================================================
save_partial() {
    if [[ $DRY_RUN -eq 1 ]]; then return 0; fi
    if python3 "$EXPS/analyze_all.py" >> "$EXPS/analysis_progress.log" 2>&1; then
        echo "  [$(date +%H:%M:%S)] Resultados parciais salvos em experiments/results.csv"
    else
        echo "  [$(date +%H:%M:%S)] AVISO: falha ao salvar parcial (ver analysis_progress.log)"
    fi
}


# =============================================================================
# Main
# =============================================================================
echo "======================================================"
echo "  AODV vs OLSR — Suite completa de experimentos"
echo "  Topologias: ${RUN_TOPOLOGIES[*]}"
if [[ $DRY_RUN -eq 1 ]]; then
    echo "  MODO: DRY RUN"
fi
echo "======================================================"

ensure_configs

TOTAL_START=$(date +%s)

# ── 1. grid-25 ────────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "grid-25"; then
    echo ""
    echo "━━━ Topologia  1/10: Grid 5x5 (25 nos) ━━━━━━━━━━━━"
    run_pair \
        "grid-25   AODV" "$EXPS/grid_25nodes/config_AODV_seed100" "$EXPS/grid_25nodes/out_AODV" \
        "grid-25   OLSR" "$EXPS/grid_25nodes/config_OLSR_seed101" "$EXPS/grid_25nodes/out_OLSR" \
        25 5 240
    save_partial
fi

# ── 2. random-50 ──────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-50"; then
    echo ""
    echo "━━━ Topologia  2/10: Random  50 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-50  AODV" "$EXPS/random_50nodes/config_AODV_seed200" "$EXPS/random_50nodes/out_AODV" \
        "random-50  OLSR" "$EXPS/random_50nodes/config_OLSR_seed201" "$EXPS/random_50nodes/out_OLSR" \
        50 5 500
    save_partial
fi

# ── 3. random-75 ──────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-75"; then
    echo ""
    echo "━━━ Topologia  3/10: Random  75 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-75  AODV" "$EXPS/random_75nodes/config_AODV_seed210" "$EXPS/random_75nodes/out_AODV" \
        "random-75  OLSR" "$EXPS/random_75nodes/config_OLSR_seed211" "$EXPS/random_75nodes/out_OLSR" \
        75 5 600
    save_partial
fi

# ── 4. random-100 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-100"; then
    echo ""
    echo "━━━ Topologia  4/10: Random 100 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-100 AODV" "$EXPS/random_100nodes/config_AODV_seed300" "$EXPS/random_100nodes/out_AODV" \
        "random-100 OLSR" "$EXPS/random_100nodes/config_OLSR_seed301" "$EXPS/random_100nodes/out_OLSR" \
        100 5 650
    save_partial
fi

# ── 5. random-150 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-150"; then
    echo ""
    echo "━━━ Topologia  5/10: Random 150 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-150 AODV" "$EXPS/random_150nodes/config_AODV_seed310" "$EXPS/random_150nodes/out_AODV" \
        "random-150 OLSR" "$EXPS/random_150nodes/config_OLSR_seed311" "$EXPS/random_150nodes/out_OLSR" \
        150 5 700
    save_partial
fi

# ── 6. random-200 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-200"; then
    echo ""
    echo "━━━ Topologia  6/10: Random 200 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-200 AODV" "$EXPS/random_200nodes/config_AODV_seed400" "$EXPS/random_200nodes/out_AODV" \
        "random-200 OLSR" "$EXPS/random_200nodes/config_OLSR_seed401" "$EXPS/random_200nodes/out_OLSR" \
        200 5 750
    save_partial
fi

# ── 7. random-300 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-300"; then
    echo ""
    echo "━━━ Topologia  7/10: Random 300 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-300 AODV" "$EXPS/random_300nodes/config_AODV_seed410" "$EXPS/random_300nodes/out_AODV" \
        "random-300 OLSR" "$EXPS/random_300nodes/config_OLSR_seed411" "$EXPS/random_300nodes/out_OLSR" \
        300 5 750
    save_partial
fi

# ── 8. random-500 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-500"; then
    echo ""
    echo "━━━ Topologia  8/10: Random 500 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-500 AODV" "$EXPS/random_500nodes/config_AODV_seed500" "$EXPS/random_500nodes/out_AODV" \
        "random-500 OLSR" "$EXPS/random_500nodes/config_OLSR_seed501" "$EXPS/random_500nodes/out_OLSR" \
        500 5 800
    save_partial
fi

# ── 9. random-750 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-750"; then
    echo ""
    echo "━━━ Topologia  9/10: Random 750 nos ━━━━━━━━━━━━━━━"
    run_pair \
        "random-750 AODV" "$EXPS/random_750nodes/config_AODV_seed510" "$EXPS/random_750nodes/out_AODV" \
        "random-750 OLSR" "$EXPS/random_750nodes/config_OLSR_seed511" "$EXPS/random_750nodes/out_OLSR" \
        750 5 850
    save_partial
fi

# ── 10. random-1000 ───────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-1000"; then
    echo ""
    echo "━━━ Topologia 10/10: Random 1000 nos ━━━━━━━━━━━━━━"
    run_pair \
        "random-1000 AODV" "$EXPS/random_1000nodes/config_AODV_seed600" "$EXPS/random_1000nodes/out_AODV" \
        "random-1000 OLSR" "$EXPS/random_1000nodes/config_OLSR_seed601" "$EXPS/random_1000nodes/out_OLSR" \
        1000 5 900
    save_partial
fi

TOTAL_END=$(date +%s)
TOTAL=$((TOTAL_END - TOTAL_START))

echo ""
echo "======================================================"
echo "  Concluido em $((TOTAL/60))m $((TOTAL%60))s"
echo ""
echo "  Para analisar todos os resultados:"
echo "    python3 $EXPS/analyze_all.py"
echo "======================================================"
