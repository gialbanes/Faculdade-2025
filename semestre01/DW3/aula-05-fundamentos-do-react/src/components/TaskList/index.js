import styles from "@/components/TaskList/TaskList.module.css"

const TaskList = ({ tasks }) => {
  if (tasks.length === 0) {
    return <p>Não há tarefas no momento.</p>;
  }

  return (
    <>
      <div>
        <h4 className="title">Lista de tarefas:</h4>
        <ol className={styles.items}>
          {/* Iterando sobre a lista de tarefas */}
          {tasks.map((task) => (
            <li key={task.id}>{task.text}</li>
          ))}
        </ol>
      </div>
    </>
  );
};
export default TaskList;
