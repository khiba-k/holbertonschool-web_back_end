export default function guardrail(mathFunction) {
  try {
    const queue = [mathFunction, 'Guardrail was processed'];
    return queue;
  } catch (e) {
    const queue = [e, 'Guardrail was processed'];
    return queue;
  }
}
