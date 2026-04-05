#!/bin/bash
# Diagnóstico NS-3 + MeshSim compilation issues

echo "=== DIAGNÓSTICO NS-3 + MeshSim ==="
echo ""

# Verificar se NS-3 existe
echo "1. Procurando NS-3..."
if [ -d "ns-3.47" ]; then
    echo "   ✓ ns-3.47/ encontrado"
    
    # Verificar build
    if [ -d "ns-3.47/build" ]; then
        echo "   ✓ Build directory existe"
        
        # Verificar libs
        if [ -d "ns-3.47/build/lib" ]; then
            LIB_COUNT=$(ls ns-3.47/build/lib/ 2>/dev/null | wc -l)
            echo "   ✓ Build/lib/ tem $LIB_COUNT files"
        else
            echo "   ✗ Build/lib/ NÃO ENCONTRADO - NS-3 pode não ter compilado"
        fi
        
        # Verificar headers
        if [ -d "ns-3.47/build/include/ns3" ]; then
            HEADER_COUNT=$(ls ns-3.47/build/include/ns3/ 2>/dev/null | wc -l)
            echo "   ✓ Build/include/ns3/ tem $HEADER_COUNT headers"
        else
            echo "   ✗ Build/include/ns3/ NÃO ENCONTRADO"
        fi
    else
        echo "   ✗ ns-3.47/build/ NÃO EXISTE - NS-3 não foi compilado!"
    fi
else
    echo "   ✗ ns-3.47/ não encontrado"
fi

echo ""
echo "2. Variáveis de ambiente atuais:"
echo "   NS3_DIR=$NS3_DIR"
echo "   PKG_CONFIG_PATH=$PKG_CONFIG_PATH"
echo ""

echo "3. MeshSim build status:"
if [ -d "MeshSim-master/build" ]; then
    echo "   ✓ MeshSim/build/ existe"
    if [ -f "MeshSim-master/build/CMakeCache.txt" ]; then
        echo "   ⚠ CMake anterior em cache - precisa limpar!"
    fi
else
    echo "   • MeshSim/build/ não existe (será criado)"
fi

echo ""
echo "=== RECOMENDAÇÃO ==="
echo ""
echo "Execute os seguintes comandos EM ORDEM:"
echo ""
echo "# 1. Compilar NS-3 (se ainda não feito):"
echo "cd ns-3.47"
echo "mkdir -p build && cd build"
echo "cmake .. -DCMAKE_BUILD_TYPE=Release"
echo "make -j8"
echo "cd ../.."
echo ""
echo "# 2. Definir variáveis de ambiente:"
echo "export NS3_DIR=\$(pwd)/ns-3.47/build"
echo "export PKG_CONFIG_PATH=\$NS3_DIR/lib/pkgconfig:\$PKG_CONFIG_PATH"
echo "export LD_LIBRARY_PATH=\$NS3_DIR/lib:\$LD_LIBRARY_PATH"
echo ""
echo "# 3. Limpar MeshSim build anterior:"
echo "rm -rf MeshSim-master/build"
echo ""
echo "# 4. Recompilar MeshSim:"
echo "cd MeshSim-master"
echo "mkdir build && cd build"
echo "cmake .. -DNS3_DIR=\$NS3_DIR"
echo "make -j8"
