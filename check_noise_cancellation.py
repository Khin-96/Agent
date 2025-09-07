# check_noise_cancellation.py
from livekit.plugins import noise_cancellation
import inspect

print("Available in noise_cancellation module:")
for name, obj in inspect.getmembers(noise_cancellation):
    if not name.startswith('_'):
        print(f"  {name}: {type(obj)}")