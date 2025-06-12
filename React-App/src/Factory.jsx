// Button Factory Component
function Button({ type, label, onClick }) {
  const getButtonStyle = () => {
    switch (type) {
      case 'primary':
        return { backgroundColor: 'blue', color: 'white' };
      case 'danger':
        return { backgroundColor: 'red', color: 'white' };
      default:
        return { backgroundColor: 'gray', color: 'black' };
    }
  };

  return (
    <button onClick={onClick} style={getButtonStyle()}>
      {label}
    </button>
  );
}

// Usage
function Factory() {
  return (
    <div>
      <Button type="primary" label="Submit" onClick={() => alert('Submitted!')} />
      <Button type="danger" label="Delete" onClick={() => alert('Deleted!')} />
      <Button type="default" label="Cancel" onClick={() => alert('Cancelled!')} />
    </div>
  );
}

export default Factory;