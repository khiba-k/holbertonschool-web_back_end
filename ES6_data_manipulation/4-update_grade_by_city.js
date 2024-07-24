export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  function filterByCity(obj) {
    if (obj.location === city) return true;
    return false;
  }

  const trueCity = getListStudents.filter(filterByCity);

  function addGrades(obj) {
    return { ...obj, grade: newGrades };
  }

  return trueCity.map(addGrades);
}
