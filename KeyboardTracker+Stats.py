#Keyboard Tracker. Idea from hollowknight
import keyboard
import keyboard

pressed_keys = set()
nums = {}
nums2 = {}
def on_key_event(e):
    key = f'{e.name}'
    if key not in pressed_keys:
        print(key)
        pressed_keys.add(key)
    elif e.event_type == keyboard.KEY_UP:
        nums[key] = nums.get(key, 0) + 1
        pressed_keys.remove(key)
    
# Hook the keyboard event
keyboard.hook(on_key_event)
# Keep the script running
keyboard.wait('esc')
keyboard.unhook_all()
print("\n")
for key, count in nums.items():
    print(f'{key}: {count} times pressed')
