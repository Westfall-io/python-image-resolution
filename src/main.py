# Output is to verify a resolution requirement
#pixel_pitch_micron = 0.0055 #mm
#focal_length = 31.69 # cm
#distance = 500 #km
import time
start_time = time.time()

def main():
    try:
        pixel_pitch_micron = "{{ digitalforge('pixel_pitch') }}" #mm
        focal_length = "{{ digitalforge('focal_length') }}" # cm
        distance = "{{ digitalforge('semimajor_axis')}}" #km
    except:
        # Defaults if this didn't work
        pixel_pitch_micron = 0.0055
        focal_length = 31.69
        distance = 500

    # Spatial resolution is the image projection of a single pixel on the ground
    import math

    # Convert pitch and focal length to angle
    ifov = (pixel_pitch_micron/1e3)/(focal_length/1e2) #rad

    gsd = distance*1000 * math.tan(ifov)

    print(gsd) #m
    with open('image_resolution_output.txt', 'w') as f:
        f.write(gsd)

if __name__ == '__main__':
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
