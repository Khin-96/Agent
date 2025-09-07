# test_vision.py
import vision_tools

# Test basic functionality
print("Testing vision tools...")

# Test camera access
frame, error = vision_tools.capture_frame()
if error:
    print(f"Camera error: {error}")
else:
    print(f"Camera working! Frame shape: {frame.shape}")

# Test individual functions
print("\nTesting functions:")
print("Finger count:", vision_tools.count_fingers())
print("Objects:", vision_tools.detect_objects())
print("Scene:", vision_tools.describe_scene())
print("Faces:", vision_tools.detect_faces())
print("Text:", vision_tools.read_text())