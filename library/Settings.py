from library import RegionInterest

connect_to_robot = True
connect_to_sonar = False
connect_to_thermal = True

# GPOI nnr

trigger_pin1 = 26
trigger_pin2 = 19

echo_pin1 = 20
echo_pin2 = 16

# Thermal
thermal_roi = [[-0.5, 0, 0.25], [-0.25, 0, 0.25], [0, 0, 0.25], [0.25, 0, 0.25], [0.5, 0, 0.25]]
thermal_fov = 110 #width of FOV in angles

# Microphone
microphone_band_centers = [500, 20000, 10]  # start, end, n
microphone_band_width = 1000

# Camera settings
camera_width = 160
camera_height = 80
camera_iso = 800
camera_shutter_speed = 100000  # in microseconds
camera_roi = [[-0.5, -0.5, 0.5], [-0.25, -0.5, 0.5], [0, -0.5, 0.5], [0.25, -0.5, 0.5], [0.5, -0.5, 0.5]]
camera_greyscale = True
camera_fov = 160 #width of FOV in angles

if __name__ == "__main__":
    camera_regions = RegionInterest.Regions(200,100)
    camera_regions.set_centers(camera_roi)
    camera_regions.plot_current_masks()

    thermal_regions = RegionInterest.Regions(200,100)
    thermal_regions.set_centers(thermal_roi)
    thermal_regions.plot_current_masks()

