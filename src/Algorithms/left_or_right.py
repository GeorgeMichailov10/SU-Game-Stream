import asyncio

async def left_or_right(frame, coordinates):
    frame_horizontal_center = frame.shape[1] / 2
    frame_vertical_center = frame.shape[0] / 2

    object_center_x = (coordinates[0] + coordinates[2]) / 2
    object_center_y = (coordinates[1] + coordinates[3]) / 2

    if object_center_x < frame_horizontal_center and object_center_y < frame_vertical_center:
        return 'top-left'
    elif object_center_x >= frame_horizontal_center and object_center_y < frame_vertical_center:
        return 'top-right'
    elif object_center_x < frame_horizontal_center and object_center_y >= frame_vertical_center:
        return 'bottom-left'
    else:
        return 'bottom-right'
    
