import requests

def get_user_postcode() -> None:
    return input("Write one UK postcode to be validated: ")

def validate_postcode(postcode: str) -> None:
    url = f'https://api.postcodes.io/postcodes/{postcode}'
    
    response = requests.get(url)
    
    if response.status_code == 200: 
        data = response.json()
        if data['status'] == 200:
            formatted_postcode = data['result']['postcode']
            region_name = data['result']['admin_district']
            country_name = data['result']['country']
            return True, formatted_postcode, region_name, country_name
        else:
            return False, None, None, None
    else:
        return False, None, None, None

def verify_postcode() -> None:
    while True:
        postcode_to_validate = get_user_postcode()
        
        is_valid, formatted_postcode, region_name, country_name = validate_postcode(postcode_to_validate)
        
        if is_valid: 
            if formatted_postcode == postcode_to_validate:
                print(f"Your postcode '{postcode_to_validate}' is valid.\nIt belongs to: {region_name}/{country_name} and it's correctly formatted.")
            else:
                print(f"Your postcode '{postcode_to_validate}' is valid.\nIt belongs to: {region_name}/{country_name}\nand it could be correctly formatted as: {formatted_postcode}")
        else: 
            print(f"Sorry to inform but your postcode '{postcode_to_validate}' is invalid in the UK. \nPlease try again.\n")
        
        retry = input("Would you like to check again another postcode? (y/n): ").strip().lower()
        if retry != 'y':
            print("Thanks for using my program bye.\n")
            break 
