from CancerDetector import detect_cancer

def will_the_startup_succeed(
	startup_name: str = "Start it up",
	buzzwords: list[str] = [
		"Cloud", "Cyber", "Quantum", "Kubernetes",
		"Stealth", "Deep Tech", "Quick Win",
		"Big Data", "AI", "ML",
	],
	amount_of_workers: int = 3,
) -> bool:
	return detect_cancer()
