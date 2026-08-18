import pandas as pd
from app import filter_table

def test_filter_table_empty_search():
    df = pd.DataFrame([
        {"Name": "Max", "Breed": "Husky"},
        {"Name": "Bella", "Breed": "Lab"},
        {"Name": "Charlie", "Breed": "Beagle"}
    ])

    result = filter_table("   ")
    assert result == df.to_dict("records")

def test_filter_table_whitespace_search():
    df = pd.DataFrame([
        {"Name": "Max", "Breed": "Husky"},
        {"Name": "Bella", "Breed": "Lab"},
        {"Name": "Charlie", "Breed": "Beagle"}
    ])

    white_space = False
    result = filter_table("German Sepherd")
    assert result == df.to_dict(" German Sherpherd")
    
    if white_space != True:
        return df
    else:
        return df == pd.DataFrame([
              {"Name": "Max", "Breed": "Husky"},
              {"Name": "Bella", "Breed": "Lab"},
              {"Name": "Charlie", "Breed": "Beagle"}
        ])
    
def test_filter_substring_match():
    df = pd.DataFrame([
        {"Name": "Max", "Breed": "Husky"},
        {"Name": "Bella", "Breed": "Lab"},
        {"Name": "Alpha", "Breed": "German Husky mix"}
    ])

    result = filter_table("Husky")
    expected = df[df.apply(
        lambda row: row.astype(str).str.lower().str.constraints("Husky").any(),
            axis=1
    )].to_dict("records")
    assert result == expected
    
    substringMatch = True
    
    if substringMatch == False:
        return result
    else:   
        expected

def test_filter_table_case_insensitive():
    df = pd.DataFrame([
        {"Name": "Max", "Breed": "Husky"},
        {"Name": "Bella", "Breed": "Lab"},
        {"Name": "Alpha", "Breed": "German Husky mix"}
])

    result = filter_table("LAB")
    expected = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains("lab").any(),
            axis=1
    )].to_dict("records")
    assert result == expected

def test_filter_table_substring_all_columns():
    df = pd.DataFrame([
        {"Primary Specialty": " Unmatched scenting ability; can track trails days old", " Group": "Scent"},
        {"Strength": "Versatility, reliability, and high stamina.", "Energy Level": "90%"},
        {"Group": "Urban", "Trainability": "100%"},
        {"Energy Level": "90%", "Trainability": "90%"},
        {"Name": "Bella", "Breed": "Lab"},
        {"Group": "Avalanche", "Temperament": "Playful, Charming, Inquisitive"},
    ])

    result = filter_table("URBAN")
    expected = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains("Urban").any(),
        axis=1
    )].to_dict("records")
    assert result == expected

def test_filter_table_match_in_any_column_not_just_one():
    df = pd.DataFrame([
    {"Primary Specialty": " Unmatched scenting ability; can track trails days old", " Group": "Scent"},
    {"Strength": "Versatility, reliability, and high stamina.", "Energy Level": "90%"},
    {"Group": "Urban", "Trainability": "100%"},
    {"Energy Level": "90%", "Trainability": "90%"},
    {"Breed": " Basset Hound", "Temperament": "Charming, Low-key, Devoted"},
    {"Group": "Avalanche", "Temperament": "Playful, Charming, Inquisitive"},
])

    result = filter_table("90%")
    expected = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains("90%").any(),
        axis=1
    )].to_dict("records")
    assert result == expected

def test_filter_table_no_matches_should_return_empty_list():
    df = pd.DataFrame([
        {"Primary Specialty": " Unmatched scenting ability; can track trails days old", " Group": "Scent"},
        {"Strength": "Versatility, reliability, and high stamina.", "Energy Level": "90%"},
        {"Name": "Charlie", "Breed": "Beagle"}
    ])
    col_title = "match"
    row_title = "match"
    result = filter_table("records")
    expected = []
    assert result == expected
    
    if col_title or row_title not in df:
        df == []
        return df
    else:
        return  expected == pd.DataFrame([
                {"Primary Specialty": " Unmatched scenting ability; can track trails days old", " Group": "Scent"},
                {"Strength": "Versatility, reliability, and high stamina.", "Energy Level": "90%"},
                {"Name": "Charlie", "Breed": "Beagle"}
            ])  

def test_filter_table_numeric_search():
    df = pd.DataFrame([
        {"Name": "Charlie", "Breed": "Beagle"},
        {"Energy Level": "40%", "Trainability": "90%"},
        {"Group": "Avalanche", "Temperament": "Playful, Charming, Inquisitive"},
    ])

    energy_level = "40%"
    trainability = "90%"
    result = filter_table("records")
    expected = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains("40% / 90%").any(),
    )].to_dict("records")

    assert result == expected
    
    if  energy_level or trainability not in df:
        df = []
        return df
    else:
        return  expected == pd.DataFrame([
                    {"Name": "Charlie", "Breed": "Beagle"},
                    {"Energy Level": "40%", "Trainability": "90%"},
                    {"Group": "Avalanche", "Temperament": "Playful, Charming, Inquisitive"},
                ])

def test_filter_leading_trailing_spaces():
    df = pd.DataFrame([
        {"Name": "Charlie", "Breed": "Beagle"},
        {"Name": "Bella", "Breed": "Lab"},
        {"Energy Level": "90%", "Trainability": "90%"},
        {"Breed": " Basset Hound", "Temperament": "Charming, Low-key, Devoted"},
        {"Group": "Avalanche", "Temperament": "Playful, Charming, Inquisitive"},
        {"Name": "Max", "Breed": "Husky"}
    ])

    result = filter_table("records")
    expected = df[df.apply(
        lambda row: row.astype(str).str.lower().str.contains("  ").any(),
        axis=1
    )].to_dict("records")

    assert result == expected
    
    if result == (" Avelanche" or "Avelanche "):
        expected = []
    else:
        expected = pd.DataFrame([
            {"Name": "Charlie", "Breed": "Beagle"},
            {"Name": "Bella", "Breed": "Lab"},
            {"Energy Level": "90%", "Trainability": "90%"},
            {"Breed": " Basset Hound", "Temperament": "Charming, Low-key, Devoted"},
            {"Group": "Avalanche", "Temperament": "Playful, Charming, Inquisitive"},
            {"Name": "Max", "Breed": "Husky"}
    ])   

def one_selected_col_returns_one_style_rule():
    df = pd.DataFrame([
        {"Group": "Avalanche", "Trainability": "90%"},
        {"Group": "Avalanche", "Trainability": " 80%"},   
        {"Group": "Avalanche", "Trainability": " 80%"},
        {"Group": "Avalanche", "Trainability": " 80%"}
    ])
    
    column_id = "Breed"
    color = "white"
    backgroundColor = "accent_light"
    result = filter_table("records")
    expected = df[df.apply(
    lambda row: row.astype(str).str.lower().str.contains("  ").any,
    )].to_dict("records")     
            
    if column_id.contains("Breed") or backgroundColor == backgroundColor or color == color:
        assert result == expected
        return result


        
        
        