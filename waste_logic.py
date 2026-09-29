"""
Waste Analysis Logic
Knowledge base and keyword matching for Smart Waste Management Assistant.
"""

WASTE_KNOWLEDGE_BASE = {
    "Plastic Waste": {
        "keywords": ["plastic", "bottle", "polythene", "wrapper", "container", "bag", "bucket", "tub", "jug", "pvc", "styrofoam", "packaging", "straw"],
        "waste_category": "Plastic Waste",
        "disposal_method": "Place it in the appropriate recyclable/plastic-waste collection bin.",
        "environmental_impact": "Plastic waste can remain in the environment for a long period and may contribute to land and water pollution.",
        "basic_handling": "Empty and rinse the container or bottle completely before recycling. Compress to save space.",
        "recommended_action": "Send it to an authorized recycling or plastic waste collection facility."
    },
    "Paper Waste": {
        "keywords": ["paper", "newspaper", "cardboard", "book", "notebook", "magazine", "envelope", "box", "carton", "flyer", "document"],
        "waste_category": "Paper Waste",
        "disposal_method": "Bundle neatly and place in the paper recycling bin or drop off at a paper collection center.",
        "environmental_impact": "Paper waste is biodegradable, but excessive waste contributes to deforestation and landfill volume.",
        "basic_handling": "Keep paper clean and dry. Flatten cardboard boxes to optimize bin storage space.",
        "recommended_action": "Hand over to paper recycling units or community paper collection drives."
    },
    "Glass Waste": {
        "keywords": ["glass", "jar", "pane", "glassware", "vial", "window glass", "mirror", "glass bottle"],
        "waste_category": "Glass Waste",
        "disposal_method": "Deposit in designated glass recycling collection containers.",
        "environmental_impact": "Glass is 100% recyclable infinitely, but broken glass poses safety hazards and persists indefinitely in nature.",
        "basic_handling": "Rinse out liquids or food scraps. Handle carefully to prevent breakage and wrap sharp pieces if broken.",
        "recommended_action": "Drop off intact glass containers at designated glass collection centers."
    },
    "Food Waste": {
        "keywords": ["food", "vegetable", "fruit", "leftover", "meal", "bread", "meat", "peel", "bone", "cooked food", "kitchen waste"],
        "waste_category": "Food Waste",
        "disposal_method": "Dispose of in wet/organic waste bins or use for home composting.",
        "environmental_impact": "Improperly disposed food waste can create unpleasant odors and contribute to environmental pollution.",
        "basic_handling": "Separate food scraps from packaging. Drain excess liquid before placing in wet waste bins.",
        "recommended_action": "Compost at home or send to municipal organic waste processing facilities."
    },
    "E-Waste": {
        "keywords": ["phone", "mobile", "computer", "laptop", "charger", "cable", "electronics", "display", "monitor", "tv", "keyboard", "mouse", "appliance", "circuit", "gadget", "headphone", "earphone"],
        "waste_category": "E-Waste",
        "disposal_method": "Take the electronic device to an authorized e-waste collection or recycling facility.",
        "environmental_impact": "Electronic waste may contain hazardous substances and should be handled through authorized collection or recycling channels.",
        "basic_handling": "Keep the device dry. Do not break or burn the device. Store batteries separately when possible.",
        "recommended_action": "Hand over the device to an authorized e-waste collection or recycling center."
    },
    "Metal Waste": {
        "keywords": ["metal", "aluminum", "tin", "can", "steel", "iron", "foil", "wire", "nail", "bolt", "utensil", "copper", "scrap metal"],
        "waste_category": "Metal Waste",
        "disposal_method": "Place clean metal cans and scraps in dry recyclable bins or scrap metal collection centers.",
        "environmental_impact": "Recycling metal waste conserves natural energy and raw mineral resources significantly.",
        "basic_handling": "Rinse food residue from cans. Beware of sharp metal edges when handling.",
        "recommended_action": "Sell or donate metal items to certified scrap recyclers."
    },
    "Medical Waste": {
        "keywords": ["medical", "syringe", "needle", "bandage", "medicine", "pill", "glove", "mask", "tablet", "pharmaceutical", "ointment"],
        "waste_category": "Medical Waste",
        "disposal_method": "Dispose of in dedicated biohazard waste bins or return unused medicine to pharmacies.",
        "environmental_impact": "Medical waste can harbor pathogens and active pharmaceutical chemicals that harm public health and ecosystems.",
        "basic_handling": "Place sharps (needles/syringes) in puncture-proof containers. Keep isolated from regular trash.",
        "recommended_action": "Return to hospital biohazard collection points or licensed medical waste handlers."
    },
    "Battery Waste": {
        "keywords": ["battery", "cell", "power bank", "lithium", "accumulator", "dry cell", "aa battery", "aaa battery", "button cell"],
        "waste_category": "Battery Waste",
        "disposal_method": "Drop off at dedicated battery recycling boxes or hazardous waste collection centers.",
        "environmental_impact": "Batteries contain corrosive chemicals and heavy metals that can leak into soil and groundwater if landfilled.",
        "basic_handling": "Tape battery terminals with insulating tape. Store in a cool, dry place away from flame.",
        "recommended_action": "Deposit at retail battery recycling collection boxes or municipal hazardous waste points."
    },
    "Organic/Garden Waste": {
        "keywords": ["organic", "garden", "leaf", "grass", "plant", "twig", "compost", "branch", "weed", "flower", "yard waste", "wood chip"],
        "waste_category": "Organic/Garden Waste",
        "disposal_method": "Compost in garden pits or place in green yard-waste collection bins.",
        "environmental_impact": "Organic garden waste decomposes naturally into nutrient-rich soil compost, reducing landfill volume.",
        "basic_handling": "Chop large branches into smaller pieces. Avoid mixing non-biodegradable trash with garden clippings.",
        "recommended_action": "Use for home soil enrichment or community green waste composting programs."
    },
    "Textile Waste": {
        "keywords": ["textile", "cloth", "clothes", "fabric", "shirt", "pants", "rag", "cotton", "wool", "dress", "towel", "curtain", "garment", "denim"],
        "waste_category": "Textile Waste",
        "disposal_method": "Donate wearable clothes or deposit unwearable textiles in textile recycling bins.",
        "environmental_impact": "Textile manufacturing consumes intensive resources; landfilled clothing takes years to decompose and generates landfill emissions.",
        "basic_handling": "Clean and dry garments before donation. Repurpose worn-out fabrics as household cleaning rags.",
        "recommended_action": "Donate to local charities or drop off at dedicated fabric recycling bins."
    }
}


def analyze_waste_input(user_input: str) -> dict:
    """
    Analyzes user text input or category selection using simple keyword matching logic.
    Returns structured analysis information dictionary.
    """
    if not user_input or not user_input.strip():
        return {
            "waste_category": "Invalid Input",
            "disposal_method": "Unable to identify the waste type. Please provide more details or select a common waste type.",
            "environmental_impact": "No input provided.",
            "basic_handling": "Please type a waste item or select a common waste type.",
            "recommended_action": "Provide valid waste information to get guidance."
        }

    clean_input = user_input.lower().strip()

    # 1. Exact Category Name Check
    for category_name, info in WASTE_KNOWLEDGE_BASE.items():
        if clean_input == category_name.lower():
            return {
                "waste_category": info["waste_category"],
                "disposal_method": info["disposal_method"],
                "environmental_impact": info["environmental_impact"],
                "basic_handling": info["basic_handling"],
                "recommended_action": info["recommended_action"]
            }

    # 2. Keyword Matching with Scoring
    best_match_category = None
    max_score = 0

    for category_name, info in WASTE_KNOWLEDGE_BASE.items():
        score = 0
        for kw in info["keywords"]:
            if kw in clean_input:
                score += 1
        if score > max_score:
            max_score = score
            best_match_category = info

    if best_match_category:
        return {
            "waste_category": best_match_category["waste_category"],
            "disposal_method": best_match_category["disposal_method"],
            "environmental_impact": best_match_category["environmental_impact"],
            "basic_handling": best_match_category["basic_handling"],
            "recommended_action": best_match_category["recommended_action"]
        }

    # 3. Fallback if no keywords matched
    return {
        "waste_category": "Unclassified / Unknown Waste",
        "disposal_method": "Unable to identify the waste type. Please provide more details or select a common waste type.",
        "environmental_impact": "Unknown environmental impact due to unclassified waste category.",
        "basic_handling": "Handle with care and keep separated from standard recyclable streams until identified.",
        "recommended_action": "Consult local waste-management authorities for proper disposal guidance."
    }
