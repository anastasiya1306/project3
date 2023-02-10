import requests
from utils import*

URL = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230209T193511Z&X-Amz-Expires=86400&X-Amz-Signature=16e7f9d6cd13b759cbc65cb9cb7fd96e55fb2b959e2da25e426ed99e0507478c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"


def main():
    result = requests.get(URL)
    result_data = result.json()
    data = get_filtered_operation(result_data)
    data = get_from_operation(data)
    transaction = get_last_five_operation(data)


    for i in transaction:
        print(f"{get_date(i)} {get_description(i)}\n"
              f"{get_from(i)} -> {get_to(i)}\n"
              f"{get_operation_amount(i)}", end='\n\n')

if __name__ == "__main__":
    main()