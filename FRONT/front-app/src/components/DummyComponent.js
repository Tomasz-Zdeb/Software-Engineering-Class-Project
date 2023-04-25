import { useState } from 'react';
import { Button } from 'react-bootstrap';

const DummyComponent = () => {
  const [color, setColor] = useState('green');

  const handleClick = () => {
    setColor(color === 'green' ? 'red' : 'green');
  };

  return (
    <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
      <div style={{ backgroundColor: color, width: 100, height: 100 }} data-testid="DummyComponentSquare"></div>
      <Button onClick={handleClick} className="ms-3" data-testid="DummyComponentButton">
        Toggle Color
      </Button>
    </div>
  );
};

export default DummyComponent;
