###Camera

if player reaches certain position player gets put to speed 0

then level is moving in the speed of the player in opposite direction

scrool_x(self)
    x: get player center
    y: direction player is moving to

    if playerx < number and dirextion < 0:
        worldShiftSpeed = player speed
        player speed = 0
    elif player > number and directionx > 0:
        worldShiftSpeed = - player speed
        playerspeed = 0
    else:
        world shit = 0
        player = speed

