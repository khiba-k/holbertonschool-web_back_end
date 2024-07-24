import getListStudentIds from "./1-get_list_student_ids";

export default function getStudentIdsSum(getListStudents) {
  
  let studentIds = getListStudentIds(getListStudent);

  function addIds(id1, idOthers) {
    return id1 + idOthers;
  }

  return studentIds.reduce(addIds);
}
