export default function guardrail(mathFunction) {
  try {
    const myReturn = mathFunction;
    const queue = [myReturn, 'Guarderail was processed'];
    return queue;
  } catch (e) {
    const queue = [e, 'Guardrail was processed'];
    return queue;
  }
}
