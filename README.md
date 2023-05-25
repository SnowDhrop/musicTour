# Description

MusicTour generates a JSON or returns all the styles and/or artists in the world.

It is based on the website https://everynoise.com/

# Quick start

```python
import musicTour
musicTour.getAll() # Generates a JSON with all styles and artists in the world
```

# Warning

Generating all the styles and/or artists can take several dozens of minutes.

# Parameters

The function musicTour.getAll() can take 3 arguments.
By default, they are all set to True.

# musicTour.getAll(styles, artists, output)

All three arguments are booleans.

To generate a JSON, you have to set the third argument to True.

Examples:

```python
musicTour.getAll(True, True, True) # generates a JSON of all styles and artists.

musicTour.getAll(False, True, True) # generates a JSON of all artists.

musicTour.getAll(True, False, True) # generates a JSON of all styles.
```

When you just want to return the value in a variable, you can set the third argument to False:

Examples:

```python
allArtistsStyles = musicTour.getAll(True, True, False)
print(allArtistsStyles) # Prints all styles and artists

musicTour.getAll(False, True, False)# returns all artists.

musicTour.getAll(True, False, False)# returns all styles.
```
