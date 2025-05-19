#Python slicing is safe:

movie="The GodFather"

print(movie[4:100])   # Godfather
# Going beyond the actual index in slicing does not raise an error, It just stops at the end of the string

print(movie[40:100])  # Empty string
#Python does not raise an error — it just returns nothing
print('END')

print(movie[:])                 # The Godfather  <- By default start to end
print(movie[::-1])              # rehtaFdoG ehT  <-reverse string
print(movie[:4],movie[4:])      # The  Godfather. By default, print() inserts a space between arguments when using commas
print(movie[:4]+movie[4:])      # The Godfather.
print(movie[::-1][::-1])        # The Godfather. reverese string to reverse string, so the o/p is original string itself
print('Reverse'[::-1])          # esreveR


