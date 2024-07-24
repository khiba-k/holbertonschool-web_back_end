export default function getListStudentIds(arr) {
  let boolean = Array.isArray(arr);

  if (!boolean) {
    return [];
  }

  function getId(obj) {
    return obj.id;
  }

  return arr.map(getId);
}
