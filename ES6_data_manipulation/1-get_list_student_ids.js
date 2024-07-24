export default function getListStudentIds(arr) {
  function getId(obj) {
    return obj.id;
  }

  return arr.map(getId);
}
