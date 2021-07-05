def groupArrayElements(arr, n):
    sizeperchunk = -(-len(arr)//n)  # alternativly use math.ceil on arr/n

    output = []
    # start from 0, go til n*sizeperchunk and increment by sizeperchunk (so that there are no overlaps)
    # i represents the start index of each chunk
    for i in range(0, n*sizeperchunk, sizeperchunk):
        output.append(arr[i:i+sizeperchunk])

    return output


print(groupArrayElements([1, 2, 3, 4, 5], 3))
