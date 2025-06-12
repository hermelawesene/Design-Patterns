function Card({ children }) {
  return <div style={{ 
    border: '1px solid #ccc',
    borderRadius: '8px',
    padding: '16px',
    margin: '10px'
  }}>{children}</div>;
}

function CardHeader({ children }) {
  return <div style={{ 
    fontSize: '1.2em',
    marginBottom: '10px'
  }}>{children}</div>;
}

function CardBody({ children }) {
  return <div>{children}</div>;
}

function Composite() {
  return (
    <Card>
      <CardHeader>Welcome!</CardHeader>
      <CardBody>
        <p>This is a composite component example.</p>
        <Card> {/* Card within a Card! */}
          <CardHeader>Nested Card</CardHeader>
          <CardBody>Composite pattern allows this!</CardBody>
        </Card>
      </CardBody>
    </Card>
  );
}

// Try adding more nested cards!
export default Composite;