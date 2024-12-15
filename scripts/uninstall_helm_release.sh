#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <namespace>"
    exit 1
fi

NAMESPACE=$1

# List all Helm releases in the namespace
RELEASES=$(helm list --namespace "$NAMESPACE" --all --short)

if [ $? -ne 0 ]; then
    echo "Error listing Helm releases. Please ensure Helm is installed and configured correctly."
    exit 1
fi

if [ -z "$RELEASES" ]; then
    echo "No Helm releases found in namespace: $NAMESPACE"
    exit 0
fi

# Uninstall all releases in the namespace
for RELEASE in $RELEASES; do
    echo "Uninstalling release: $RELEASE from namespace: $NAMESPACE"
    helm uninstall "$RELEASE" --namespace "$NAMESPACE"
    if [ $? -ne 0 ]; then
        echo "Failed to uninstall release: $RELEASE"
    else
        echo "Successfully uninstalled release: $RELEASE"
    fi
done