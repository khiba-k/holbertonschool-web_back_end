export default function getStudentIdsSum(getListStudents) {
  function addIds(obj1, objectOthers) {
    return obj1.id + objectOthers.id;
  }

  return getListStudents.reduce(addIds);
}
