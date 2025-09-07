# check_room_input_options.py
from livekit.agents import RoomInputOptions
import inspect

# Check what parameters RoomInputOptions accepts
sig = inspect.signature(RoomInputOptions.__init__)
print("RoomInputOptions parameters:")
for param_name, param in sig.parameters.items():
    if param_name != 'self':
        print(f"  {param_name}: {param.default}")