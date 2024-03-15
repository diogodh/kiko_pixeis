import cv2

# Function to handle mouse events
def click_event(event, x, y, flags, param):
    global dot_counts

    # Single click
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        dot_counts['green'] += 1

    # Double click
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        dot_counts['blue'] += 2
        dot_counts['green'] -= 1
        update_image()  # Update the image immediately after adding the blue dot

    # Show the image with the dots and counts
    update_image()


# Function to update the image with dot counts
def update_image():
    global img  # Make sure to declare img as global
    
    # Create a copy of the original image to work with
    img_with_counts = img.copy()

    # Draw dot counts on the copied image
    dot_counts_text = "Green: {}   Blue: {}    Total: {}".format(dot_counts['green'], dot_counts['blue'], sum(dot_counts.values()))
    cv2.putText(img_with_counts, dot_counts_text, (10, img_with_counts.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # Show the updated image
    cv2.imshow('image', img_with_counts)


# Prompt for the image file
image_path = input("Enter the path to the image: ")

# Read the image
img = cv2.imread(image_path)

# Initialize dot count dictionary
dot_counts = {'green': 0, 'blue': 0}

# Display the image
cv2.imshow('image', img)

# Set the mouse callback function
cv2.setMouseCallback('image', click_event)

# Wait for any key to be pressed and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
