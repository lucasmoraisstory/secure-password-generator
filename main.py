# Gerador de Senhas Seguras para Desenvolvedores
import random
import string

def gerador_senhas():
    print("🔒 GERADOR DE SENHAS SEGURAS 🔒")
    print("-" * 35)
    
    try:
        tamanho = int(input("Digite o comprimento desejado para a senha (mínimo 8): "))
        
        if tamanho < 8:
            print("⚠️ Segurança baixa! Definindo tamanho automático para 8 caracteres.")
            tamanho = 8
            
        # Pools de caracteres (Letras, números e símbolos)
        caracteres = string.ascii_letters + string.digits + string.punctuation
        
        # Gera a senha combinando caracteres aleatórios
        senha_gerada = "".join(random.choice(caracteres) for i in range(tamanho))
        
        print("\n" + "=" * 35)
        print(f"🔑 Senha gerada com sucesso:\n👉 {senha_gerada}")
        print("=" * 35)
        print("Dica: Nunca compartilhe suas chaves de acesso e senhas!")
        
    except ValueError:
        print("\n❌ Erro: Insira um número inteiro válido.")

if __name__ == "__main__":
    gerador_senhas()
