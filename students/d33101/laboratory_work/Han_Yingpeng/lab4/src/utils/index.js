const getCreatorName = (creator) =>
  creator.username || `${creator.first_name} ${creator.last_name}`;

export { getCreatorName };

export default { getCreatorName };
