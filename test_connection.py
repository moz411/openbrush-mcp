#!/usr/bin/env python3
"""
Script de test pour vérifier la connexion à l'API Open Brush
"""

import httpx
import sys

API_BASE_URL = "http://localhost:40074/api/v1"

def test_connection():
    """Teste la connexion à l'API Open Brush"""
    print("🔍 Test de connexion à l'API Open Brush...")
    print(f"📡 URL: {API_BASE_URL}")
    print()
    
    try:
        # Test 1: Vérifier que l'API répond
        print("1️⃣ Test de connectivité...")
        response = httpx.get(API_BASE_URL, params={"help": ""}, timeout=5.0)
        response.raise_for_status()
        print("   ✅ API accessible!")
        print()
        
        # Test 2: Tester une commande simple
        print("2️⃣ Test d'une commande simple (undo)...")
        response = httpx.get(API_BASE_URL, params={"undo": ""}, timeout=5.0)
        response.raise_for_status()
        print("   ✅ Commande exécutée avec succès!")
        print(f"   📄 Réponse: {response.text[:100]}...")
        print()
        
        # Test 3: Obtenir l'aide
        print("3️⃣ Récupération de l'aide...")
        response = httpx.get(API_BASE_URL, params={"help": ""}, timeout=5.0)
        if response.status_code == 200:
            print("   ✅ Page d'aide disponible!")
            print(f"   📄 Taille de la réponse: {len(response.text)} caractères")
        print()
        
        print("=" * 60)
        print("✨ Tous les tests ont réussi!")
        print("=" * 60)
        print()
        print("Le serveur MCP devrait fonctionner correctement.")
        print("Vous pouvez maintenant:")
        print("  1. Configurer Claude Desktop avec ce serveur")
        print("  2. Lancer: python openbrush_mcp_server.py")
        
        return True
        
    except httpx.ConnectError:
        print("   ❌ Impossible de se connecter à l'API")
        print()
        print("Vérifiez que:")
        print("  • Open Brush est lancé")
        print("  • L'API HTTP est activée dans les paramètres")
        print("  • Le port 40074 est bien utilisé")
        return False
        
    except httpx.HTTPError as e:
        print(f"   ❌ Erreur HTTP: {e}")
        return False
        
    except Exception as e:
        print(f"   ❌ Erreur inattendue: {e}")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
