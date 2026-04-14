import random
import time

def generate_sensor_data():
    return {
        "temperature": random.uniform(40, 100),
        "vibration": random.uniform(0, 5),
        "current": random.uniform(5, 25)
    }


def run_simulation():
    print("🔄 Starting Industrial Simulation...")

    for i in range(50):
        data = generate_sensor_data()

        print(f"""
        Cycle {i+1}
        Temp: {data['temperature']:.2f}
        Vibration: {data['vibration']:.2f}
        Current: {data['current']:.2f}
        -------------------------
        """)

        time.sleep(0.5)