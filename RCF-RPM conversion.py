def calculate_rcf(radius_cm, rpm):

    rcf = 11.2 * radius_cm * (rpm / 1000) ** 2
    return rcf

def main():
    radius_cm = float(input("Enter the radius of the rotor (in centimeters): "))
    rpm = float(input("Enter the revolutions per minute (RPM) of the rotor: "))

    rcf = calculate_rcf(radius_cm, rpm)

    print(f"The Relative Centrifugal Force (RCF) is: {rcf} g")


if __name__ == "__main__":
    main()

def calculate_rpm(rcf, radius_cm):

    rpm = ((rcf / (11.2 * radius_cm)) ** 0.5) * 1000
    return rpm


def main():
    rcf = float(input("Enter the Relative Centrifugal Force (RCF) in g units: "))
    radius_cm = float(input("Enter the radius of the rotor (in centimeters): "))

    rpm = calculate_rpm(rcf, radius_cm)

    print(f"The revolutions per minute (RPM) of the rotor is: {rpm}")


if __name__ == "__main__":
    main()
