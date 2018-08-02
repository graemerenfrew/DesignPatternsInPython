from computer import Computer

#Long parameter lists like this can be a sign there's a better way to approach
#this problem
computer = Computer(case="SuperCase 300",
                    mainboard = "BoardX 100",
                    cpu="386x",
                    memory="4GB",
                    hard_drive="40MB Seagate IDE",
                    video_card="GPUMPER"

)

computer.display()