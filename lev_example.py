from f1_codex import LevGuard

@LevGuard(harm_threshold=0.01)
def deploy_ai_model(data, simulated_harm=0.005):
    print("Model deployed successfully!")

if __name__ == "__main__":
    deploy_ai_model("patient_data")
