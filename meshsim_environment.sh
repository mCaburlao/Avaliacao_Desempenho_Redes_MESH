#!/bin/bash
# REPRODUCIBILITY: MeshSim Environment Setup
# Generated: automatic diagnostic
# Use this file to ensure consistent environment for all simulations

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export NS3_DIR="${PROJECT_ROOT}/ns-3-dev/build"
export PKG_CONFIG_PATH="${NS3_DIR}/lib/pkgconfig:${PKG_CONFIG_PATH}"
export LD_LIBRARY_PATH="${NS3_DIR}/lib:${LD_LIBRARY_PATH}"

echo "MeshSim Environment Loaded:"
echo "  NS3_DIR=$NS3_DIR"
echo "  LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
