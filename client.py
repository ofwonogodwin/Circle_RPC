import requests

print("Circle Area Calculator (RPC Client)")

while True:
    user_input = input("Enter radius (0 to exit): ")

    try:
        radius = float(user_input)
    except ValueError:
        print("Error: Please enter a valid number")
        continue

    if radius == 0:
        print("Exiting...")
        break

    try:
        response = requests.post(
            "http://127.0.0.1:5000/calculate_area",
            json={"radius": radius}
        )
        data = response.json()

        if data['status'] == 'success':
            print(f"Result: Area = {data['result']} (calculated by remote function '{data['function']}')")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.ConnectionError:
        print("Error: Server not running. Please start the server first.")
