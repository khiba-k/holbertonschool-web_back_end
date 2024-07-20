import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const classRoom1 = new ClassRoom(19);
  const classRoom2 = new ClassRoom(20);
  const classRoom3 = new ClassRoom(34);

  const classRooms = [`ClassRoom { _maxStudentSize: ${classRoom1}}`,
    `ClassRoom { _maxStudentSize: ${classRoom2}}`,
    `ClassRoom { _maxStudentSize: ${classRoom3}}`,
  ];
  return classRooms;
}
