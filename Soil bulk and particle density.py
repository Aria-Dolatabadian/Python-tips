def calculate_bulk_density(mass_of_soil, volume_of_soil):
    bulk_density = mass_of_soil / volume_of_soil
    return bulk_density

def calculate_particle_density(mass_of_soil, volume_of_solid_particles):
    particle_density = mass_of_soil / volume_of_solid_particles
    return particle_density

def main():
    mass_of_soil = float(input("Enter the mass of the soil sample (in grams): "))
    volume_of_soil = float(input("Enter the volume of the soil sample (in cubic centimeters): "))
    volume_of_solid_particles = float(input("Enter the volume of solid particles in the soil sample (in cubic centimeters): "))

    bulk_density = calculate_bulk_density(mass_of_soil, volume_of_soil)
    particle_density = calculate_particle_density(mass_of_soil, volume_of_solid_particles)

    print("\nBulk Density of the soil: {:.2f} g/cm^3".format(bulk_density))
    print("Particle Density of the soil: {:.2f} g/cm^3".format(particle_density))

if __name__ == "__main__":
    main()
