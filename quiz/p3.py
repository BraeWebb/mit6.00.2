def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    if songs[0][2] <= max_size:
        disk = [songs[0][0]]
        disk_used = songs[0][2]
    else:
        return []
    songs = sorted(songs, key=lambda song: song[2])
    for song in songs:
        if song[0] in disk:
            continue
        if song[2] <= max_size - disk_used:
            disk.append(song[0])
            disk_used += song[2]
        else:
            break
    return disk

print(song_playlist([('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], 12.2))
print(song_playlist([('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], 11))
print(song_playlist([('aa', 4, 4), ('bb', 5, 7), ('cc', 5, 6), ('dd', 2, 1)], 3))