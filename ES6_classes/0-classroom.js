export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }

  get numOfRooms() {
    return this._maxStudentsSize;
  }
}
