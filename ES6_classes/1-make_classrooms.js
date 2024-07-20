import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const ClassRoomClass = ClassRoom;
  const classRoom1 = new ClassRoomClass(19);
  const classRoom2 = new ClassRoomClass(20);
  const classRoom3 = new ClassRoomClass(34);

  const classRooms = [`ClassRoom { _maxStudentSize: ${classRoom1.numOfRooms}}`,
    `ClassRoom { _maxStudentSize: ${classRoom2.numOfRooms}}`,
    `ClassRoom { _maxStudentSize: ${classRoom3.numOfRooms}}`,
  ];
  return classRooms;
}
