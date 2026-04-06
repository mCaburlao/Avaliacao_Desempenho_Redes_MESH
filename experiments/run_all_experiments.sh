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
        chain-9|grid-25|random-50|random-100|random-200|random-500|random-1000|random-2000) RUN_TOPOLOGIES+=("$arg") ;;
        *) echo "Argumento desconhecido: $arg"; exit 1 ;;
    esac
done

# Sem argumento de topologia = roda tudo
if [ ${#RUN_TOPOLOGIES[@]} -eq 0 ]; then
    RUN_TOPOLOGIES=("chain-9" "grid-25" "random-50" "random-100" "random-200" "random-500" "random-1000" "random-2000")
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
# Funcao: gerar configs se necessario
# =============================================================================
ensure_configs() {
    local NEED_GEN=0
    for topo in "${RUN_TOPOLOGIES[@]}"; do
        case "$topo" in
            grid-25)
                [ -d "$EXPS/grid_25nodes/config_AODV_seed100" ] || NEED_GEN=1 ;;
            random-50)
                [ -d "$EXPS/random_50nodes/config_AODV_seed200" ] || NEED_GEN=1 ;;
            random-100)
                [ -d "$EXPS/random_100nodes/config_AODV_seed300" ] || NEED_GEN=1 ;;
            random-200)
                [ -d "$EXPS/random_200nodes/config_AODV_seed400" ] || NEED_GEN=1 ;;
            random-500)
                [ -d "$EXPS/random_500nodes/config_AODV_seed500" ] || NEED_GEN=1 ;;
            random-1000)
                [ -d "$EXPS/random_1000nodes/config_AODV_seed600" ] || NEED_GEN=1 ;;
            random-2000)
                [ -d "$EXPS/random_2000nodes/config_AODV_seed700" ] || NEED_GEN=1 ;;
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

# ── 1. chain-9 ────────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "chain-9"; then
    echo ""
    echo "━━━ Topologia 1/8: Cadeia Linear 9 nos ━━━━━━━━━━━━━"

    run_sim "chain-9  AODV" \
        "$EXPS/pilot_100_aodv_olsr/config_AODV_seed42" \
        "$EXPS/pilot_100_aodv_olsr/out_AODV" \
        9 9 400

    run_sim "chain-9  OLSR" \
        "$EXPS/pilot_100_aodv_olsr/config_OLSR_seed43" \
        "$EXPS/pilot_100_aodv_olsr/out_OLSR" \
        9 9 400
    save_partial
fi

# ── 2. grid-25 ────────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "grid-25"; then
    echo ""
    echo "━━━ Topologia 2/8: Grid 5x5 (25 nos) ━━━━━━━━━━━━━━"

    run_sim "grid-25  AODV" \
        "$EXPS/grid_25nodes/config_AODV_seed100" \
        "$EXPS/grid_25nodes/out_AODV" \
        25 25 500

    run_sim "grid-25  OLSR" \
        "$EXPS/grid_25nodes/config_OLSR_seed101" \
        "$EXPS/grid_25nodes/out_OLSR" \
        25 25 500
    save_partial
fi

# ── 3. random-50 ──────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-50"; then
    echo ""
    echo "━━━ Topologia 3/8: Random 50 nos ━━━━━━━━━━━━━━━━━━"

    run_sim "random-50 AODV" \
        "$EXPS/random_50nodes/config_AODV_seed200" \
        "$EXPS/random_50nodes/out_AODV" \
        50 50 600

    run_sim "random-50 OLSR" \
        "$EXPS/random_50nodes/config_OLSR_seed201" \
        "$EXPS/random_50nodes/out_OLSR" \
        50 50 600
    save_partial
fi

# ── 4. random-100 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-100"; then
    echo ""
    echo "━━━ Topologia 4/8: Random 100 nos ━━━━━━━━━━━━━━━━━"

    run_sim "random-100 AODV" \
        "$EXPS/random_100nodes/config_AODV_seed300" \
        "$EXPS/random_100nodes/out_AODV" \
        100 100 700

    run_sim "random-100 OLSR" \
        "$EXPS/random_100nodes/config_OLSR_seed301" \
        "$EXPS/random_100nodes/out_OLSR" \
        100 100 700
    save_partial
fi

# ── 5. random-200 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-200"; then
    echo ""
    echo "━━━ Topologia 5/8: Random 200 nos ━━━━━━━━━━━━━━━━━"

    run_sim "random-200 AODV" \
        "$EXPS/random_200nodes/config_AODV_seed400" \
        "$EXPS/random_200nodes/out_AODV" \
        200 200 800

    run_sim "random-200 OLSR" \
        "$EXPS/random_200nodes/config_OLSR_seed401" \
        "$EXPS/random_200nodes/out_OLSR" \
        200 200 800
    save_partial
fi

# ── 6. random-500 ─────────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-500"; then
    echo ""
    echo "━━━ Topologia 6/8: Random 500 nos ━━━━━━━━━━━━━━━━━"

    run_sim "random-500 AODV" \
        "$EXPS/random_500nodes/config_AODV_seed500" \
        "$EXPS/random_500nodes/out_AODV" \
        500 20 700

    run_sim "random-500 OLSR" \
        "$EXPS/random_500nodes/config_OLSR_seed501" \
        "$EXPS/random_500nodes/out_OLSR" \
        500 20 700
    save_partial
fi

# ── 7. random-1000 ───────────────────────────────────────
 if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-1000"; then
    echo ""
    echo "━━━ Topologia 7/8: Random 1000 nos ━━━━━━━━━━━━━━━━"

    run_sim "random-1000 AODV" \
        "$EXPS/random_1000nodes/config_AODV_seed600" \
        "$EXPS/random_1000nodes/out_AODV" \
        1000 20 800

    run_sim "random-1000 OLSR" \
        "$EXPS/random_1000nodes/config_OLSR_seed601" \
        "$EXPS/random_1000nodes/out_OLSR" \
        1000 20 800
    save_partial
fi

# ── 8. random-2000 ───────────────────────────────────────
if printf '%s\n' "${RUN_TOPOLOGIES[@]}" | grep -qx "random-2000"; then
    echo ""
    echo "━━━ Topologia 8/8: Random 2000 nos ━━━━━━━━━━━━━━━━"

    run_sim "random-2000 AODV" \
        "$EXPS/random_2000nodes/config_AODV_seed700" \
        "$EXPS/random_2000nodes/out_AODV" \
        2000 20 900

    run_sim "random-2000 OLSR" \
        "$EXPS/random_2000nodes/config_OLSR_seed701" \
        "$EXPS/random_2000nodes/out_OLSR" \
        2000 20 900
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
echo ""
echo "  Para analisar so o piloto:"
echo "    python3 $EXPS/pilot_100_aodv_olsr/analyze_pilot.py"
echo "======================================================"
